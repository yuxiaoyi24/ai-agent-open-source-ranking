#!/usr/bin/env python3
"""Build compact local and remote data consumed by the WeChat mini program."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RANKINGS_DIR = ROOT / "data" / "rankings"
OUTPUT = ROOT / "wechat-miniprogram" / "miniprogram" / "data" / "rankings.js"
PUBLIC_OUTPUT = ROOT / "data" / "miniprogram" / "latest.json"

MODULE_COLORS = [
    "#4cc9f0", "#4895ef", "#4361ee", "#7209b7", "#b5179e", "#f72585",
    "#f97316", "#f59e0b", "#84cc16", "#22c55e", "#14b8a6", "#06b6d4",
    "#0ea5e9", "#8b5cf6", "#a855f7", "#ec4899", "#ef4444", "#eab308",
]


def latest_file() -> Path:
    files = sorted(RANKINGS_DIR.glob("*.json"))
    if not files:
        raise SystemExit("No ranking JSON found")
    return files[-1]


def compact_project(item: dict) -> dict:
    fields = (
        "project", "slug", "repo", "module", "kind", "license", "priority",
        "architect_note", "stars", "star_delta", "weekly_star_delta",
        "weekly_growth_rate", "composite_score", "momentum_score",
        "activity_score", "health_score", "pushed_at", "description",
    )
    return {key: item.get(key) for key in fields}


def main() -> None:
    source = latest_file()
    payload = json.loads(source.read_text(encoding="utf-8"))
    projects = [item for item in payload.get("projects", []) if not item.get("archived")]
    module_names = []
    for item in projects:
        if item.get("module") not in module_names:
            module_names.append(item["module"])

    modules = []
    top_projects = {}
    for index, module in enumerate(module_names):
        candidates = [item for item in projects if item.get("module") == module]
        composite = sorted(
            candidates,
            key=lambda item: (item.get("composite_score") or 0, item.get("stars") or 0),
            reverse=True,
        )[:5]
        momentum = sorted(
            [item for item in candidates if (item.get("momentum_score") or 0) > 0 and (item.get("weekly_star_delta") or 0) > 0],
            key=lambda item: (item.get("momentum_score") or 0, item.get("star_delta") or 0, item.get("stars") or 0),
            reverse=True,
        )[:5]
        compact_composite = [compact_project(item) for item in composite]
        compact_momentum = [compact_project(item) for item in momentum]
        modules.append({
            "key": module,
            "label": module,
            "color": MODULE_COLORS[index % len(MODULE_COLORS)],
            "count": len(candidates),
            "note": (composite[0].get("architect_note") if composite else "暂无可展示项目") or "暂无可展示项目",
            "composite": compact_composite,
            "momentum": compact_momentum,
        })
        for item in compact_composite + compact_momentum:
            top_projects[item["slug"]] = item

    discoveries = payload.get("discoveries", {})
    output_payload = {
        "schema_version": 1,
        "date": payload.get("date"),
        "previous_snapshot_date": payload.get("previous_snapshot_date"),
        "generated_at": payload.get("generated_at"),
        "module_count": len(modules),
        "project_count": len(projects),
        "candidate_count": sum(len(items) for items in discoveries.values()),
        "modules": modules,
        "projects": list(top_projects.values()),
    }
    serialized = json.dumps(output_payload, ensure_ascii=False, separators=(",", ":"))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        "// Generated from {}. Do not edit by hand.\nmodule.exports = {};\n".format(source.relative_to(ROOT), serialized),
        encoding="utf-8",
    )
    PUBLIC_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC_OUTPUT.write_text(serialized + "\n", encoding="utf-8")
    print("wrote {}".format(OUTPUT))
    print("wrote {}".format(PUBLIC_OUTPUT))


if __name__ == "__main__":
    main()
