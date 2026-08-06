#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional
from zoneinfo import ZoneInfo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agent_landscape.core import (  # noqa: E402
    find_previous_snapshot,
    load_config,
    load_projects,
    load_snapshot,
    rank_projects,
    ranking_payload,
    render_report,
    snapshot_payload,
    top_by_module,
    write_json,
    write_text,
)
from agent_landscape.dashboard import render_dashboard  # noqa: E402
from agent_landscape.github_client import GitHubClient  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh GitHub metadata and build weekly Agent module rankings."
    )
    parser.add_argument(
        "--provider",
        choices=("auto", "graphql", "html", "offline"),
        default="auto",
        help="Metadata provider. auto uses GraphQL with GITHUB_TOKEN, otherwise public HTML.",
    )
    parser.add_argument(
        "--date",
        help="Ranking date in YYYY-MM-DD. Defaults to today in the configured timezone.",
    )
    parser.add_argument(
        "--module",
        action="append",
        dest="modules",
        help="Refresh one module for a dry-run smoke test. May be repeated.",
    )
    parser.add_argument(
        "--discover",
        action="store_true",
        help="Search GitHub for new candidates and place them in the watchlist section.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the report without writing snapshots or reports.",
    )
    parser.add_argument("--workers", type=int, default=8, help="Parallel HTML workers.")
    parser.add_argument("--top", type=int, help="Override Top N from config.")
    return parser.parse_args()


def resolve_date(value: Optional[str], timezone_name: str) -> date:
    if value:
        return date.fromisoformat(value)
    return datetime.now(ZoneInfo(timezone_name)).date()


def main() -> int:
    args = parse_args()
    config_path = PROJECT_ROOT / "config" / "ranking.json"
    project_path = PROJECT_ROOT / "data" / "agent-open-source-projects.csv"
    snapshot_dir = PROJECT_ROOT / "data" / "snapshots"
    report_dir = PROJECT_ROOT / "reports" / "weekly"

    config = load_config(config_path)
    module_config = config["modules"]
    selected_modules: List[str] = args.modules or list(module_config.keys())
    unknown_modules = sorted(set(selected_modules) - set(module_config.keys()))
    if unknown_modules:
        raise SystemExit("Unknown module(s): {}".format(", ".join(unknown_modules)))
    if args.modules and not args.dry_run:
        raise SystemExit("Partial --module refreshes must use --dry-run to protect snapshot history")

    as_of = resolve_date(args.date, config["timezone"])
    baseline_date = date.fromisoformat(config["baseline_date"])
    projects = [
        project for project in load_projects(project_path) if project.module in selected_modules
    ]
    selected_config: Dict[str, dict] = {
        module: module_config[module] for module in module_config if module in selected_modules
    }

    client = GitHubClient(workers=max(1, args.workers))
    states = client.fetch_projects(projects, provider=args.provider)
    previous_path = find_previous_snapshot(snapshot_dir, as_of)
    previous_date, previous_states = load_snapshot(previous_path)

    ranked = rank_projects(
        projects=projects,
        states=states,
        as_of=as_of,
        baseline_date=baseline_date,
        previous_date=previous_date,
        previous_states=previous_states,
        weights=config["weights"],
    )
    discoveries = (
        client.discover(
            module_config=selected_config,
            curated_slugs=[project.slug for project in load_projects(project_path)],
            modules=selected_modules,
        )
        if args.discover
        else {}
    )
    top_n = args.top or int(config["top_n"])
    rankings = top_by_module(ranked, list(selected_config.keys()), top_n)
    failures = [item for item in ranked if item.fetch_error]
    report = render_report(
        as_of=as_of,
        previous_date=previous_date,
        rankings=rankings,
        module_config=selected_config,
        discoveries=discoveries,
        fetch_failures=failures,
    )

    providers = sorted({state.provider for state in states.values()})
    provider_label = ",".join(providers)
    if args.dry_run:
        print(report)
        print(
            "DRY RUN: {} projects, {} modules, provider={}, failures={}".format(
                len(projects), len(selected_config), provider_label, len(failures)
            ),
            file=sys.stderr,
        )
        return 0

    snapshot_file = snapshot_dir / "{}.json".format(as_of.isoformat())
    ranking_file = PROJECT_ROOT / "data" / "rankings" / "{}.json".format(as_of.isoformat())
    dated_report = report_dir / "{}-agent-open-source-ranking.md".format(as_of.isoformat())
    latest_report = report_dir / "latest.md"
    dated_dashboard = report_dir / "{}-agent-open-source-ranking.html".format(as_of.isoformat())
    latest_dashboard = report_dir / "latest.html"

    write_json(snapshot_file, snapshot_payload(as_of, provider_label, states.values()))
    write_json(
        ranking_file,
        ranking_payload(as_of, previous_date, ranked, discoveries),
    )
    write_text(dated_report, report)
    write_text(latest_report, report)
    dashboard = render_dashboard(
        as_of=as_of,
        previous_date=previous_date,
        rankings=rankings,
        module_config=selected_config,
        discoveries=discoveries,
        fetch_failures=failures,
    )
    write_text(dated_dashboard, dashboard)
    write_text(latest_dashboard, dashboard)

    print("snapshot={}".format(snapshot_file))
    print("ranking={}".format(ranking_file))
    print("report={}".format(dated_report))
    print("latest={}".format(latest_report))
    print("dashboard={}".format(dated_dashboard))
    print("latest_dashboard={}".format(latest_dashboard))
    print(
        "summary=projects:{} modules:{} provider:{} failures:{} discoveries:{}".format(
            len(projects),
            len(selected_config),
            provider_label,
            len(failures),
            sum(len(items) for items in discoveries.values()),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
