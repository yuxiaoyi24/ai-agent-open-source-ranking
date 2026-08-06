from __future__ import annotations

import html
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from http.client import IncompleteRead
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen
from xml.etree import ElementTree

from .core import Project, RepositoryState


USER_AGENT = "agent-landscape-weekly-ranker/1.0"
STAR_PATTERN = re.compile(r'aria-label="([0-9,.]+) users starred this repository"')
CANONICAL_PATTERN = re.compile(
    r'<meta property="og:url" content="https://github\.com/([^"/]+/[^"/]+)"'
)


class GitHubClient:
    def __init__(
        self,
        token: Optional[str] = None,
        timeout: int = 25,
        workers: int = 8,
    ) -> None:
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.timeout = timeout
        self.workers = workers

    def fetch_projects(
        self,
        projects: Sequence[Project],
        provider: str = "auto",
    ) -> Dict[str, RepositoryState]:
        selected_provider = provider
        if provider == "auto":
            selected_provider = "graphql" if self.token else "html"
        if selected_provider == "graphql":
            if not self.token:
                raise ValueError("GraphQL provider requires GITHUB_TOKEN")
            return self._fetch_graphql(projects)
        if selected_provider == "html":
            return self._fetch_html_parallel(projects)
        if selected_provider == "offline":
            return {
                project.slug.lower(): RepositoryState(
                    slug=project.slug,
                    canonical_repo=project.repo,
                    stars=project.baseline_stars,
                    pushed_at=None,
                    updated_at=None,
                    head_oid=None,
                    archived=False,
                    license=project.license,
                    provider="offline",
                )
                for project in projects
            }
        raise ValueError("Unknown provider: {}".format(provider))

    def _fetch_graphql(self, projects: Sequence[Project]) -> Dict[str, RepositoryState]:
        states: Dict[str, RepositoryState] = {}
        for start in range(0, len(projects), 40):
            batch = projects[start : start + 40]
            aliases = []
            for index, project in enumerate(batch):
                owner, name = project.slug.split("/", 1)
                aliases.append(
                    """
                    r{index}: repository(owner: {owner}, name: {name}) {{
                      nameWithOwner
                      url
                      stargazerCount
                      isArchived
                      pushedAt
                      updatedAt
                      licenseInfo {{ spdxId }}
                      defaultBranchRef {{
                        target {{ ... on Commit {{ oid committedDate }} }}
                      }}
                    }}
                    """.format(index=index, owner=json.dumps(owner), name=json.dumps(name))
                )
            query = "query {\n" + "\n".join(aliases) + "\n}"
            payload = self._request_json(
                "https://api.github.com/graphql",
                method="POST",
                body={"query": query},
                authenticated=True,
            )
            if payload.get("errors"):
                raise RuntimeError("GitHub GraphQL error: {}".format(payload["errors"]))
            data = payload["data"]
            for index, project in enumerate(batch):
                item = data.get("r{}".format(index))
                if not item:
                    states[project.slug.lower()] = self._failed_state(
                        project, "Repository not found through GraphQL", "graphql"
                    )
                    continue
                target = ((item.get("defaultBranchRef") or {}).get("target") or {})
                states[project.slug.lower()] = RepositoryState(
                    slug=item["nameWithOwner"],
                    canonical_repo=item["url"],
                    stars=int(item["stargazerCount"]),
                    pushed_at=item.get("pushedAt") or target.get("committedDate"),
                    updated_at=item.get("updatedAt"),
                    head_oid=target.get("oid"),
                    archived=bool(item.get("isArchived")),
                    license=(item.get("licenseInfo") or {}).get("spdxId") or project.license,
                    provider="graphql",
                )
        return states

    def _fetch_html_parallel(self, projects: Sequence[Project]) -> Dict[str, RepositoryState]:
        states: Dict[str, RepositoryState] = {}
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {executor.submit(self._fetch_html_one, project): project for project in projects}
            for future in as_completed(futures):
                project = futures[future]
                try:
                    state = future.result()
                except Exception as error:  # noqa: BLE001 - preserve remaining weekly refresh
                    state = self._failed_state(project, str(error), "html")
                states[project.slug.lower()] = state
        return states

    def _fetch_html_one(self, project: Project) -> RepositoryState:
        page = self._request_text(project.repo)
        star_match = STAR_PATTERN.search(page)
        if not star_match:
            raise RuntimeError("Could not parse star count")
        stars = int(star_match.group(1).replace(",", ""))
        canonical_match = CANONICAL_PATTERN.search(page)
        canonical_slug = html.unescape(canonical_match.group(1)) if canonical_match else project.slug
        canonical_repo = "https://github.com/{}".format(canonical_slug)
        archived = "This repository was archived" in page or "is archived by the owner" in page

        pushed_at = None
        head_oid = None
        try:
            feed = self._request_text(canonical_repo + "/commits.atom")
            root = ElementTree.fromstring(feed)
            namespace = {"atom": "http://www.w3.org/2005/Atom"}
            entry = root.find("atom:entry", namespace)
            if entry is not None:
                updated = entry.findtext("atom:updated", default="", namespaces=namespace)
                identifier = entry.findtext("atom:id", default="", namespaces=namespace)
                pushed_at = updated or None
                head_oid = identifier.rsplit("/", 1)[-1] if identifier else None
        except (HTTPError, URLError, ElementTree.ParseError):
            pass

        now = datetime.now(timezone.utc).isoformat()
        return RepositoryState(
            slug=canonical_slug,
            canonical_repo=canonical_repo,
            stars=stars,
            pushed_at=pushed_at,
            updated_at=now,
            head_oid=head_oid,
            archived=archived,
            license=project.license,
            provider="html",
        )

    def discover(
        self,
        module_config: Mapping[str, Mapping[str, Any]],
        curated_slugs: Iterable[str],
        modules: Optional[Sequence[str]] = None,
    ) -> Dict[str, List[Dict[str, Any]]]:
        curated = {slug.lower() for slug in curated_slugs}
        selected = set(modules or module_config.keys())
        delay = 2.1 if self.token else 6.5
        discoveries: Dict[str, List[Dict[str, Any]]] = {}

        for module, config in module_config.items():
            if module not in selected:
                continue
            query = config["query"]
            endpoint = (
                "https://api.github.com/search/repositories?q={}&sort=stars&order=desc&per_page=15"
            ).format(quote_plus(query))
            try:
                payload = self._request_json(endpoint, authenticated=bool(self.token))
            except Exception as error:  # noqa: BLE001 - report discovery failure without killing refresh
                discoveries[module] = [
                    {
                        "full_name": "discovery-error",
                        "url": "https://github.com/search",
                        "stars": 0,
                        "match_score": 0,
                        "description": str(error),
                    }
                ]
                time.sleep(delay)
                continue

            candidates = []
            for item in payload.get("items", []):
                full_name = item["full_name"]
                if full_name.lower() in curated:
                    continue
                description = item.get("description") or ""
                match_score = self._keyword_match(
                    full_name + " " + description,
                    config.get("keywords", []),
                )
                if match_score == 0:
                    continue
                candidates.append(
                    {
                        "full_name": full_name,
                        "url": item["html_url"],
                        "stars": int(item["stargazers_count"]),
                        "updated_at": item.get("updated_at"),
                        "pushed_at": item.get("pushed_at"),
                        "archived": bool(item.get("archived")),
                        "license": (item.get("license") or {}).get("spdx_id"),
                        "description": description,
                        "match_score": match_score,
                    }
                )
            discoveries[module] = sorted(
                candidates,
                key=lambda item: (item["match_score"], item["stars"]),
                reverse=True,
            )[:5]
            time.sleep(delay)
        return discoveries

    @staticmethod
    def _keyword_match(text: str, keywords: Sequence[str]) -> int:
        lowered = text.lower()
        return sum(1 for keyword in keywords if keyword.lower() in lowered)

    def _request_text(self, url: str) -> str:
        request = Request(url, headers=self._headers(authenticated=False))
        for attempt in range(3):
            try:
                with urlopen(request, timeout=self.timeout) as response:
                    return response.read().decode("utf-8", errors="replace")
            except HTTPError as error:
                if error.code < 500 or attempt == 2:
                    raise
            except (URLError, TimeoutError, IncompleteRead):
                if attempt == 2:
                    raise
            time.sleep(0.5 * (2**attempt))
        raise RuntimeError("Unreachable retry state")

    def _request_json(
        self,
        url: str,
        method: str = "GET",
        body: Optional[Mapping[str, Any]] = None,
        authenticated: bool = False,
    ) -> Dict[str, Any]:
        data = json.dumps(body).encode("utf-8") if body is not None else None
        headers = self._headers(authenticated=authenticated)
        if data is not None:
            headers["Content-Type"] = "application/json"
        request = Request(url, data=data, headers=headers, method=method)
        for attempt in range(3):
            try:
                with urlopen(request, timeout=self.timeout) as response:
                    return json.loads(response.read().decode("utf-8"))
            except HTTPError as error:
                if error.code < 500 or attempt == 2:
                    raise
            except (URLError, TimeoutError, IncompleteRead):
                if attempt == 2:
                    raise
            time.sleep(0.5 * (2**attempt))
        raise RuntimeError("Unreachable retry state")

    def _headers(self, authenticated: bool) -> Dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if authenticated and self.token:
            headers["Authorization"] = "Bearer {}".format(self.token)
        elif self.token:
            headers["Authorization"] = "Bearer {}".format(self.token)
        return headers

    @staticmethod
    def _failed_state(project: Project, error: str, provider: str) -> RepositoryState:
        return RepositoryState(
            slug=project.slug,
            canonical_repo=project.repo,
            stars=project.baseline_stars,
            pushed_at=None,
            updated_at=None,
            head_oid=None,
            archived=False,
            license=project.license,
            provider=provider,
            error=error,
        )
