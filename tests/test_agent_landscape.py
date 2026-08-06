from __future__ import annotations

import json
import math
import sys
import tempfile
import unittest
from datetime import date
from http.client import IncompleteRead
from pathlib import Path
from unittest.mock import patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agent_landscape.core import (  # noqa: E402
    Project,
    RepositoryState,
    activity_score,
    delta_score,
    find_previous_snapshot,
    growth_score,
    load_config,
    load_projects,
    popularity_score,
    rank_projects,
    render_report,
    top_by_module,
)
from agent_landscape.dashboard import render_dashboard  # noqa: E402
from agent_landscape.github_client import CANONICAL_PATTERN, GitHubClient  # noqa: E402


class CoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = load_config(PROJECT_ROOT / "config" / "ranking.json")
        self.project = Project(
            module="Agent Runtime",
            project="Example",
            repo="https://github.com/example/runtime",
            baseline_stars=1000,
            priority="P0",
            license="MIT",
            kind="Agent-native",
            tags="runtime;agent",
            architect_note="runtime example",
        )

    def test_curated_csv_has_expected_scope(self) -> None:
        projects = load_projects(PROJECT_ROOT / "data" / "agent-open-source-projects.csv")
        self.assertEqual(105, len(projects))
        self.assertEqual(18, len({project.module for project in projects}))
        self.assertEqual(len(projects), len({project.slug.lower() for project in projects}))

    def test_score_functions_are_bounded(self) -> None:
        self.assertGreater(popularity_score(100000), popularity_score(1000))
        self.assertEqual(100.0, popularity_score(100000))
        self.assertEqual(0.0, delta_score(0))
        self.assertLessEqual(delta_score(100000), 100.0)
        self.assertEqual(100.0, growth_score(20.0))
        self.assertEqual(100.0, activity_score("2026-08-04T00:00:00Z", date(2026, 8, 5), None))

    def test_rank_with_history_calculates_weekly_delta(self) -> None:
        state = RepositoryState(
            slug=self.project.slug,
            canonical_repo=self.project.repo,
            stars=1070,
            pushed_at="2026-08-11T00:00:00Z",
            updated_at="2026-08-12T00:00:00Z",
            head_oid="new",
            archived=False,
            license="MIT",
            provider="test",
        )
        ranked = rank_projects(
            projects=[self.project],
            states={self.project.slug.lower(): state},
            as_of=date(2026, 8, 12),
            baseline_date=date(2026, 8, 5),
            previous_date=date(2026, 8, 5),
            previous_states={
                self.project.slug.lower(): {"stars": 1000, "head_oid": "old"}
            },
            weights=self.config["weights"],
        )[0]
        self.assertEqual(70, ranked.star_delta)
        self.assertEqual(70.0, ranked.weekly_star_delta)
        self.assertTrue(ranked.head_changed)
        self.assertIsNotNone(ranked.momentum_score)
        self.assertTrue(math.isclose(7.0, ranked.weekly_growth_rate))

    def test_first_run_has_no_momentum_ranking(self) -> None:
        state = RepositoryState(
            slug=self.project.slug,
            canonical_repo=self.project.repo,
            stars=1000,
            pushed_at=None,
            updated_at=None,
            head_oid=None,
            archived=False,
            license="MIT",
            provider="offline",
        )
        ranked = rank_projects(
            projects=[self.project],
            states={self.project.slug.lower(): state},
            as_of=date(2026, 8, 5),
            baseline_date=date(2026, 8, 5),
            previous_date=None,
            previous_states={},
            weights=self.config["weights"],
        )
        rankings = top_by_module(ranked, ["Agent Runtime"], 5)
        self.assertIsNone(ranked[0].momentum_score)
        self.assertEqual([], rankings["Agent Runtime"]["momentum"])

    def test_growth_ranking_excludes_zero_delta_projects(self) -> None:
        projects = [
            self.project,
            Project(
                module="Agent Runtime",
                project="Growing",
                repo="https://github.com/example/growing",
                baseline_stars=100,
                priority="P1",
                license="MIT",
                kind="Agent-native",
                tags="runtime",
                architect_note="growing example",
            ),
        ]
        states = {
            projects[0].slug.lower(): RepositoryState(
                projects[0].slug,
                projects[0].repo,
                1000,
                "2026-08-12T00:00:00Z",
                None,
                "same",
                False,
                "MIT",
                "test",
            ),
            projects[1].slug.lower(): RepositoryState(
                projects[1].slug,
                projects[1].repo,
                101,
                "2026-08-12T00:00:00Z",
                None,
                "new",
                False,
                "MIT",
                "test",
            ),
        }
        previous = {
            projects[0].slug.lower(): {"stars": 1000, "head_oid": "same"},
            projects[1].slug.lower(): {"stars": 100, "head_oid": "old"},
        }
        ranked = rank_projects(
            projects,
            states,
            date(2026, 8, 12),
            date(2026, 8, 5),
            date(2026, 8, 5),
            previous,
            self.config["weights"],
        )
        momentum = top_by_module(ranked, ["Agent Runtime"], 5)["Agent Runtime"]["momentum"]
        self.assertEqual(["Growing"], [item.project for item in momentum])

    def test_previous_snapshot_ignores_same_day(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            snapshot_dir = Path(directory)
            for name in ("2026-08-01.json", "2026-08-05.json", "invalid.json"):
                (snapshot_dir / name).write_text(json.dumps({}), encoding="utf-8")
            selected = find_previous_snapshot(snapshot_dir, date(2026, 8, 5))
            self.assertEqual("2026-08-01.json", selected.name)

    def test_report_contains_two_ranking_views(self) -> None:
        state = RepositoryState(
            slug=self.project.slug,
            canonical_repo=self.project.repo,
            stars=1000,
            pushed_at=None,
            updated_at=None,
            head_oid=None,
            archived=False,
            license="MIT",
            provider="offline",
        )
        ranked = rank_projects(
            [self.project],
            {self.project.slug.lower(): state},
            date(2026, 8, 5),
            date(2026, 8, 5),
            None,
            {},
            self.config["weights"],
        )
        report = render_report(
            date(2026, 8, 5),
            None,
            top_by_module(ranked, ["Agent Runtime"], 5),
            {"Agent Runtime": self.config["modules"]["Agent Runtime"]},
            {},
            [],
        )
        self.assertIn("综合 Top 5", report)
        self.assertIn("本周增长 Top 5", report)
        self.assertIn("首期仅建立基线", report)

    def test_dashboard_contains_visual_controls_and_project_links(self) -> None:
        state = RepositoryState(
            slug=self.project.slug,
            canonical_repo=self.project.repo,
            stars=1000,
            pushed_at=None,
            updated_at=None,
            head_oid=None,
            archived=False,
            license="MIT",
            provider="offline",
        )
        ranked = rank_projects(
            [self.project],
            {self.project.slug.lower(): state},
            date(2026, 8, 5),
            date(2026, 8, 5),
            None,
            {},
            self.config["weights"],
        )
        dashboard = render_dashboard(
            date(2026, 8, 5),
            None,
            top_by_module(ranked, ["Agent Runtime"], 5),
            {"Agent Runtime": self.config["modules"]["Agent Runtime"]},
            {},
            [],
        )
        self.assertIn("<!doctype html>", dashboard)
        self.assertIn("综合榜", dashboard)
        self.assertIn("本周增长榜", dashboard)
        self.assertIn("data-module=\"Agent Runtime\"", dashboard)
        self.assertIn("https://github.com/example/runtime", dashboard)
        self.assertIn("首期基线已建立", dashboard)
        self.assertIn("--chip-hue:", dashboard)
        self.assertIn("module-chip::before", dashboard)
        self.assertIn('<span class="head-rank">排名</span><span>项目</span>', dashboard)
        self.assertIn(
            "grid-template-columns:30px minmax(150px,1fr) 58px 70px 68px 58px",
            dashboard,
        )


class GitHubClientTests(unittest.TestCase):
    def test_request_text_retries_incomplete_read(self) -> None:
        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_value, traceback):
                return False

            @staticmethod
            def read() -> bytes:
                return b"ok"

        client = GitHubClient(timeout=1)
        with patch(
            "agent_landscape.github_client.urlopen",
            side_effect=[IncompleteRead(b"partial"), FakeResponse()],
        ), patch("agent_landscape.github_client.time.sleep"):
            self.assertEqual("ok", client._request_text("https://github.com/example/repo"))

    def test_canonical_repo_uses_og_url_without_title_description(self) -> None:
        page = (
            '<meta property="og:title" content="GitHub - langchain-ai/langmem" />'
            '<meta property="og:url" content="https://github.com/langchain-ai/langmem" />'
        )
        match = CANONICAL_PATTERN.search(page)
        self.assertIsNotNone(match)
        self.assertEqual("langchain-ai/langmem", match.group(1))

    def test_keyword_match_is_case_insensitive(self) -> None:
        score = GitHubClient._keyword_match(
            "Agent Runtime with OpenTelemetry",
            ["agent", "runtime", "opentelemetry", "missing"],
        )
        self.assertEqual(3, score)


if __name__ == "__main__":
    unittest.main()
