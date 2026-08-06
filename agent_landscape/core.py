from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple
from urllib.parse import urlparse


PRIORITY_SCORES = {
    "P0": 100.0,
    "P1": 75.0,
    "P2": 50.0,
    "Infrastructure": 40.0,
}


@dataclass(frozen=True)
class Project:
    module: str
    project: str
    repo: str
    baseline_stars: int
    priority: str
    license: str
    kind: str
    tags: str
    architect_note: str

    @property
    def slug(self) -> str:
        parsed = urlparse(self.repo)
        parts = [part for part in parsed.path.split("/") if part]
        if parsed.netloc.lower() != "github.com" or len(parts) < 2:
            raise ValueError("Unsupported GitHub repository URL: {}".format(self.repo))
        return "{}/{}".format(parts[0], parts[1])

    @property
    def architecture_score(self) -> float:
        return PRIORITY_SCORES.get(self.priority, 50.0)


@dataclass
class RepositoryState:
    slug: str
    canonical_repo: str
    stars: int
    pushed_at: Optional[str]
    updated_at: Optional[str]
    head_oid: Optional[str]
    archived: bool
    license: Optional[str]
    provider: str
    error: Optional[str] = None


@dataclass
class RankedProject:
    module: str
    project: str
    repo: str
    slug: str
    priority: str
    license: str
    kind: str
    tags: str
    architect_note: str
    stars: int
    previous_stars: int
    star_delta: int
    weekly_star_delta: float
    weekly_growth_rate: float
    pushed_at: Optional[str]
    head_changed: Optional[bool]
    archived: bool
    architecture_score: float
    popularity_score: float
    delta_score: float
    growth_score: float
    activity_score: float
    health_score: float
    composite_score: float
    momentum_score: Optional[float]
    fetch_error: Optional[str]


def load_config(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_projects(path: Path) -> List[Project]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        star_column = next(
            (name for name in reader.fieldnames or [] if name.startswith("stars_")),
            None,
        )
        if star_column is None:
            raise ValueError("Project CSV must contain a stars_YYYY_MM_DD column")
        projects = []
        for row in reader:
            projects.append(
                Project(
                    module=row["module"],
                    project=row["project"],
                    repo=row["repo"],
                    baseline_stars=int(row[star_column]),
                    priority=row["priority"],
                    license=row["license"],
                    kind=row["kind"],
                    tags=row["tags"],
                    architect_note=row["architect_note"],
                )
            )
    return projects


def parse_datetime(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def popularity_score(stars: int) -> float:
    return min(100.0, 20.0 * math.log10(max(0, stars) + 1.0))


def delta_score(weekly_delta: float) -> float:
    return min(100.0, (100.0 / 3.0) * math.log10(max(0.0, weekly_delta) + 1.0))


def growth_score(weekly_growth_rate: float) -> float:
    return min(100.0, max(0.0, weekly_growth_rate) * 10.0)


def activity_score(
    pushed_at: Optional[str],
    as_of: date,
    head_changed: Optional[bool],
) -> float:
    if head_changed is True:
        return 100.0
    pushed = parse_datetime(pushed_at)
    if pushed is None:
        return 50.0 if head_changed is None else 20.0
    age_days = max(0, (as_of - pushed.date()).days)
    if age_days <= 14:
        return 100.0
    if age_days <= 30:
        return 85.0
    if age_days <= 90:
        return 65.0
    if age_days <= 180:
        return 40.0
    if age_days <= 365:
        return 20.0
    return 5.0


def weighted_score(values: Mapping[str, float], weights: Mapping[str, float]) -> float:
    return round(sum(values[name] * weight for name, weight in weights.items()), 2)


def find_previous_snapshot(snapshot_dir: Path, as_of: date) -> Optional[Path]:
    candidates = []
    for path in snapshot_dir.glob("*.json"):
        try:
            snapshot_date = date.fromisoformat(path.stem)
        except ValueError:
            continue
        if snapshot_date < as_of:
            candidates.append((snapshot_date, path))
    return max(candidates, default=(None, None), key=lambda item: item[0])[1]


def load_snapshot(path: Optional[Path]) -> Tuple[Optional[date], Dict[str, Dict[str, Any]]]:
    if path is None:
        return None, {}
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    snapshot_date = date.fromisoformat(payload["date"])
    return snapshot_date, {item["slug"].lower(): item for item in payload["repositories"]}


def rank_projects(
    projects: Sequence[Project],
    states: Mapping[str, RepositoryState],
    as_of: date,
    baseline_date: date,
    previous_date: Optional[date],
    previous_states: Mapping[str, Mapping[str, Any]],
    weights: Mapping[str, Mapping[str, float]],
) -> List[RankedProject]:
    has_history = previous_date is not None
    reference_date = previous_date or baseline_date
    elapsed_days = max(1, (as_of - reference_date).days)
    weekly_factor = 7.0 / elapsed_days
    ranked = []

    for project in projects:
        state = states[project.slug.lower()]
        previous = previous_states.get(project.slug.lower())
        previous_stars = int(previous["stars"]) if previous else project.baseline_stars
        raw_delta = state.stars - previous_stars
        weekly_delta = raw_delta * weekly_factor
        weekly_growth_rate = (
            (raw_delta / previous_stars) * 100.0 * weekly_factor
            if previous_stars > 0
            else 0.0
        )
        previous_oid = previous.get("head_oid") if previous else None
        head_changed = (
            state.head_oid != previous_oid
            if state.head_oid and previous_oid
            else None
        )

        components = {
            "architecture": project.architecture_score,
            "popularity": popularity_score(state.stars),
            "weekly_star_delta": delta_score(weekly_delta),
            "weekly_growth_rate": growth_score(weekly_growth_rate),
            "activity": activity_score(state.pushed_at, as_of, head_changed),
            "health": 0.0 if state.archived else 100.0,
        }
        composite_weights = weights[
            "composite_with_history" if has_history else "composite_without_history"
        ]
        composite = weighted_score(components, composite_weights)
        momentum = weighted_score(components, weights["momentum"]) if has_history else None

        ranked.append(
            RankedProject(
                module=project.module,
                project=project.project,
                repo=state.canonical_repo or project.repo,
                slug=state.slug,
                priority=project.priority,
                license=state.license or project.license,
                kind=project.kind,
                tags=project.tags,
                architect_note=project.architect_note,
                stars=state.stars,
                previous_stars=previous_stars,
                star_delta=raw_delta,
                weekly_star_delta=round(weekly_delta, 2),
                weekly_growth_rate=round(weekly_growth_rate, 4),
                pushed_at=state.pushed_at,
                head_changed=head_changed,
                archived=state.archived,
                architecture_score=components["architecture"],
                popularity_score=round(components["popularity"], 2),
                delta_score=round(components["weekly_star_delta"], 2),
                growth_score=round(components["weekly_growth_rate"], 2),
                activity_score=round(components["activity"], 2),
                health_score=components["health"],
                composite_score=composite,
                momentum_score=momentum,
                fetch_error=state.error,
            )
        )
    return ranked


def snapshot_payload(
    as_of: date,
    provider: str,
    states: Iterable[RepositoryState],
) -> Dict[str, Any]:
    return {
        "schema_version": 1,
        "date": as_of.isoformat(),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": provider,
        "repositories": [asdict(state) for state in sorted(states, key=lambda item: item.slug.lower())],
    }


def ranking_payload(
    as_of: date,
    previous_date: Optional[date],
    ranked: Sequence[RankedProject],
    discoveries: Mapping[str, Sequence[Mapping[str, Any]]],
) -> Dict[str, Any]:
    return {
        "schema_version": 1,
        "date": as_of.isoformat(),
        "previous_snapshot_date": previous_date.isoformat() if previous_date else None,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "projects": [asdict(item) for item in ranked],
        "discoveries": discoveries,
    }


def top_by_module(
    ranked: Sequence[RankedProject],
    module_order: Sequence[str],
    top_n: int,
) -> Dict[str, Dict[str, List[RankedProject]]]:
    result = {}
    for module in module_order:
        candidates = [item for item in ranked if item.module == module and not item.archived]
        composite = sorted(
            candidates,
            key=lambda item: (item.composite_score, item.stars),
            reverse=True,
        )[:top_n]
        momentum = sorted(
            [
                item
                for item in candidates
                if item.momentum_score is not None and item.weekly_star_delta > 0
            ],
            key=lambda item: (item.momentum_score or 0.0, item.star_delta, item.stars),
            reverse=True,
        )[:top_n]
        result[module] = {"composite": composite, "momentum": momentum}
    return result


def format_stars(value: int) -> str:
    if value >= 1_000_000:
        return "{:.2f}m".format(value / 1_000_000.0)
    if value >= 1_000:
        return "{:.1f}k".format(value / 1_000.0)
    return str(value)


def render_report(
    as_of: date,
    previous_date: Optional[date],
    rankings: Mapping[str, Mapping[str, Sequence[RankedProject]]],
    module_config: Mapping[str, Mapping[str, Any]],
    discoveries: Mapping[str, Sequence[Mapping[str, Any]]],
    fetch_failures: Sequence[RankedProject],
) -> str:
    lines = [
        "# AI Agent 开源项目周榜（{}）".format(as_of.isoformat()),
        "",
        "> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。",
        "",
        "## 本期口径",
        "",
    ]
    if previous_date:
        lines.append("- 对比快照：{}，Stars 增量已折算为 7 天口径。".format(previous_date.isoformat()))
    else:
        lines.append("- 当前为首期基线，没有上一期快照；增长榜暂不代表真实周增量。")
    lines.extend(
        [
            "- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。",
            "- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。",
            "- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。",
            "",
            "## 模块周榜",
            "",
        ]
    )

    for module, config in module_config.items():
        label = config.get("label", module)
        module_rankings = rankings[module]
        lines.extend(["### {}".format(label), "", "#### 综合 Top 5", ""])
        lines.extend(
            [
                "| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |",
                "|---:|---|---:|---:|---:|---:|---|",
            ]
        )
        for index, item in enumerate(module_rankings["composite"], 1):
            delta = "+{}".format(item.star_delta) if item.star_delta >= 0 else str(item.star_delta)
            lines.append(
                "| {} | [{}]({}) | {} | {} | {:.0f} | {:.2f} | {} |".format(
                    index,
                    item.project,
                    item.repo,
                    format_stars(item.stars),
                    delta if previous_date else "—",
                    item.activity_score,
                    item.composite_score,
                    item.architect_note,
                )
            )

        lines.extend(["", "#### 本周增长 Top 5", ""])
        if not previous_date:
            lines.append("首期仅建立基线；下一次刷新后生成真实增长榜。")
        else:
            if not module_rankings["momentum"]:
                lines.append("本期未检测到正向 Stars 增量。")
            else:
                lines.extend(
                    [
                        "| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |",
                        "|---:|---|---:|---:|---:|",
                    ]
                )
                for index, item in enumerate(module_rankings["momentum"], 1):
                    lines.append(
                        "| {} | [{}]({}) | {:+.1f} | {:+.2f}% | {:.2f} |".format(
                            index,
                            item.project,
                            item.repo,
                            item.weekly_star_delta,
                            item.weekly_growth_rate,
                            item.momentum_score or 0.0,
                        )
                    )

        module_discoveries = discoveries.get(module, [])
        if module_discoveries:
            lines.extend(["", "#### 新发现观察池", ""])
            for candidate in module_discoveries[:5]:
                lines.append(
                    "- [{}]({})：{} Stars；匹配度 {}；{}".format(
                        candidate["full_name"],
                        candidate["url"],
                        candidate["stars"],
                        candidate["match_score"],
                        candidate.get("description") or "无仓库描述",
                    )
                )
        lines.append("")

    lines.extend(["## 数据质量与风险", ""])
    if fetch_failures:
        lines.append("本期以下仓库刷新失败，保留上次或基线数据：")
        lines.append("")
        for item in fetch_failures:
            lines.append("- `{}`：{}".format(item.slug, item.fetch_error))
    else:
        lines.append("- 正式候选池全部刷新成功。")
    lines.extend(
        [
            "- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。",
            "- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。",
            "",
            "## 下一步人工动作",
            "",
            "1. 复核观察池中是否有值得加入正式候选池的新项目。",
            "2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。",
            "3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。",
            "",
        ]
    )
    return "\n".join(lines)


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(content)
