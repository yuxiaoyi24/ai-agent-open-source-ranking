from __future__ import annotations

import html
import json
from datetime import date
from typing import Any, Mapping, Sequence

from .core import RankedProject, format_stars


MODULE_HUES = (198, 219, 252, 278, 314, 346, 16, 38, 68, 104, 142, 168, 188, 230, 266, 300, 8, 52)


def _esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _number(value: float, digits: int = 0) -> str:
    return ("{:,.%df}" % digits).format(value)


def _delta(value: float, previous_date: date | None) -> str:
    if previous_date is None:
        return "基线"
    return ("+" if value >= 0 else "") + _number(value, 1)


def _growth(value: float, previous_date: date | None) -> str:
    if previous_date is None:
        return "—"
    return ("+" if value >= 0 else "") + _number(value, 2) + "%"


def _activity_label(score: float) -> str:
    if score >= 85:
        return "活跃"
    if score >= 60:
        return "稳定"
    if score >= 30:
        return "偏慢"
    return "沉寂"


def _rank_item(item: RankedProject, index: int, mode: str, previous_date: date | None) -> str:
    score = item.composite_score if mode == "composite" else (item.momentum_score or 0.0)
    score_label = "综合分" if mode == "composite" else "动量分"
    delta_class = "positive" if item.weekly_star_delta > 0 else "muted"
    return """<article class="rank-item rank-{rank}" data-score="{score:.2f}">
      <div class="rank-number">{rank:02d}</div>
      <div class="rank-main">
        <div class="rank-title"><a href="{repo}" target="_blank" rel="noreferrer">{project}</a><span class="priority {priority_class}">{priority}</span></div>
        <div class="rank-meta"><span>{kind}</span><span>{license}</span><span>{activity}</span></div>
        <div class="score-track"><span style="width:{score_width:.1f}%"></span></div>
      </div>
      <div class="rank-metric"><strong>{stars}</strong><small>Stars</small></div>
      <div class="rank-metric {delta_class}"><strong>{delta}</strong><small>周增量</small></div>
      <div class="rank-metric {delta_class}"><strong>{growth}</strong><small>周增速</small></div>
      <div class="rank-score"><strong>{score:.1f}</strong><small>{score_label}</small></div>
    </article>""".format(
        rank=index,
        score=score,
        score_width=min(100.0, max(0.0, score)),
        repo=_esc(item.repo),
        project=_esc(item.project),
        priority=_esc(item.priority),
        priority_class="priority-" + _esc(item.priority).lower().replace(" ", "-"),
        kind=_esc(item.kind),
        license=_esc(item.license),
        activity=_activity_label(item.activity_score),
        score_label=score_label,
        stars=format_stars(item.stars),
        delta=_delta(item.weekly_star_delta, previous_date),
        growth=_growth(item.weekly_growth_rate, previous_date),
        delta_class=delta_class,
    )


def _module_card(
    module: str,
    config: Mapping[str, Any],
    rankings: Mapping[str, Sequence[RankedProject]],
    previous_date: date | None,
) -> str:
    composite = list(rankings.get("composite", []))
    momentum = list(rankings.get("momentum", []))
    label = config.get("label", module)
    note = composite[0].architect_note if composite else "暂无可展示项目"
    composite_html = "".join(
        _rank_item(item, index, "composite", previous_date)
        for index, item in enumerate(composite, 1)
    )
    if previous_date is None:
        momentum_html = '<div class="empty-state">首期基线已建立，下一次刷新后生成真实增长榜。</div>'
    elif not momentum:
        momentum_html = '<div class="empty-state">本期未检测到正向 Stars 增量。</div>'
    else:
        momentum_html = "".join(
            _rank_item(item, index, "momentum", previous_date)
            for index, item in enumerate(momentum, 1)
        )
    return """<section class="module-card" data-module="{module}" data-label="{label}">
      <div class="module-head"><div><span class="module-index">{module_index}</span><h2>{label}</h2><p>{note}</p></div><span class="module-count">{project_count} 个样本</span></div>
      <div class="list-head"><span class="head-rank">排名</span><span>项目</span><span>Stars</span><span>周增量</span><span>周增速</span><span>评分</span></div>
      <div class="ranking-list ranking-composite">{composite_html}</div>
      <div class="ranking-list ranking-momentum">{momentum_html}</div>
    </section>""".format(
        module=_esc(module),
        label=_esc(label),
        module_index="{0:02d}".format(config.get("order", 0) or 0),
        note=_esc(note),
        project_count=len(composite),
        composite_html=composite_html,
        momentum_html=momentum_html,
    )


def render_dashboard(
    as_of: date,
    previous_date: date | None,
    rankings: Mapping[str, Mapping[str, Sequence[RankedProject]]],
    module_config: Mapping[str, Mapping[str, Any]],
    discoveries: Mapping[str, Sequence[Mapping[str, Any]]],
    fetch_failures: Sequence[RankedProject],
) -> str:
    all_projects = [item for module in rankings.values() for item in module.get("composite", [])]
    unique_projects = {item.slug for item in all_projects}
    total_stars = sum(item.stars for item in all_projects)
    total_delta = sum(item.weekly_star_delta for item in all_projects)
    active_count = sum(item.activity_score >= 85 for item in all_projects)
    discovery_count = sum(len(items) for items in discoveries.values())
    health = "100%" if not fetch_failures else "{:.0f}%".format(
        100.0 * (len(all_projects) - len(fetch_failures)) / max(1, len(all_projects))
    )
    previous_label = previous_date.isoformat() if previous_date else "首期基线"
    module_cards = "".join(
        _module_card(module, dict(config, order=index), rankings[module], previous_date)
        for index, (module, config) in enumerate(module_config.items(), 1)
    )
    module_options = "".join(
        '<button class="filter-chip module-chip" data-filter="{module}" style="--chip-hue:{hue}">{label}</button>'.format(
            module=_esc(module),
            label=_esc(config.get("label", module)),
            hue=MODULE_HUES[index % len(MODULE_HUES)],
        )
        for index, (module, config) in enumerate(module_config.items())
    )
    watchlist = []
    for module, items in discoveries.items():
        for candidate in items[:5]:
            watchlist.append((module_config.get(module, {}).get("label", module), candidate))
    watchlist_html = "".join(
        '<a class="watch-item" href="{url}" target="_blank" rel="noreferrer"><span>{name}</span><small>{module} · {stars} Stars · 匹配度 {score}</small></a>'.format(
            url=_esc(candidate.get("url", "#")),
            name=_esc(candidate.get("full_name", "未知项目")),
            module=_esc(module),
            stars=_esc(candidate.get("stars", 0)),
            score=_esc(candidate.get("match_score", 0)),
        )
        for module, candidate in watchlist[:12]
    )
    if not watchlist_html:
        watchlist_html = '<div class="empty-state">本期没有新发现观察项。</div>'
    baseline_note = "已对比 {} 的快照，增量按 7 天标准化".format(previous_label)
    return """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>AI Agent 开源技术周榜 · {date}</title>
<style>
.list-head{{grid-template-columns:30px minmax(150px,1fr) 58px 70px 68px 58px !important;gap:8px;padding:0 8px 7px 0 !important}}.list-head span:nth-child(n+3){{text-align:right}}.list-head .head-rank{{text-align:center}}@media(max-width:650px){{.list-head{{grid-template-columns:25px minmax(110px,1fr) 52px 62px 62px 54px !important}}}}
:root{{--bg:#08111f;--panel:#101d31;--panel-2:#14243b;--line:#243752;--text:#edf4ff;--muted:#8fa3bd;--accent:#73a7ff;--teal:#49d6bd;--orange:#ffbd69;--danger:#ff7f96;--shadow:0 20px 60px rgba(0,0,0,.22)}}*{{box-sizing:border-box}}body{{margin:0;background:radial-gradient(circle at 85% -10%,#1a3157 0,#08111f 42%);color:var(--text);font:14px/1.5 Inter,-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC",sans-serif}}a{{color:inherit;text-decoration:none}}.shell{{max-width:1480px;margin:auto;padding:36px 30px 80px}}.topbar{{display:flex;justify-content:space-between;gap:24px;align-items:flex-start;margin-bottom:30px}}.eyebrow{{color:var(--teal);font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}h1{{font-size:clamp(30px,4vw,52px);line-height:1.08;margin:8px 0 12px;letter-spacing:-.045em}}.subtitle{{color:var(--muted);max-width:680px;margin:0}}.date-pill{{border:1px solid var(--line);background:rgba(16,29,49,.72);padding:12px 16px;border-radius:14px;min-width:160px;text-align:right;box-shadow:var(--shadow)}}.date-pill strong{{display:block;font-size:20px}}.date-pill span{{color:var(--muted);font-size:12px}}.kpis{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:28px}}.kpi{{background:linear-gradient(145deg,rgba(20,36,59,.96),rgba(12,24,41,.96));border:1px solid var(--line);border-radius:16px;padding:17px 18px;box-shadow:var(--shadow)}}.kpi-label{{color:var(--muted);font-size:12px}}.kpi-value{{font-size:28px;font-weight:750;letter-spacing:-.04em;margin-top:5px}}.kpi-hint{{font-size:11px;color:var(--teal);margin-top:2px}}.toolbar{{display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap;margin-bottom:18px;position:sticky;top:0;z-index:3;padding:12px 0;background:linear-gradient(#08111f 74%,transparent)}}.segmented,.filters{{display:flex;gap:7px;flex-wrap:wrap}}button{{font:inherit;color:var(--muted);background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:9px 14px;cursor:pointer;transition:.2s}}button:hover,button.active{{color:var(--text);border-color:var(--accent);background:#1b3152}}.module-chip{{display:inline-flex;align-items:center;gap:8px;color:hsl(var(--chip-hue) 68% 76%);border-color:hsl(var(--chip-hue) 55% 46% / .62);background:hsl(var(--chip-hue) 48% 20% / .34)}}.module-chip::before{{content:"";width:7px;height:7px;border-radius:50%;background:hsl(var(--chip-hue) 82% 65%);box-shadow:0 0 10px hsl(var(--chip-hue) 82% 60% / .42);flex:none}}.module-chip:hover{{color:hsl(var(--chip-hue) 90% 88%);border-color:hsl(var(--chip-hue) 78% 63%);background:hsl(var(--chip-hue) 58% 27% / .56)}}.module-chip.active{{color:#fff;border-color:hsl(var(--chip-hue) 88% 68%);background:linear-gradient(135deg,hsl(var(--chip-hue) 62% 34% / .88),hsl(var(--chip-hue) 48% 24% / .9));box-shadow:0 0 0 1px hsl(var(--chip-hue) 80% 62% / .15),0 8px 20px hsl(var(--chip-hue) 70% 15% / .24)}}.toolbar-note{{color:var(--muted);font-size:12px}}.modules{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}.module-card{{background:rgba(16,29,49,.9);border:1px solid var(--line);border-radius:18px;padding:18px;box-shadow:var(--shadow);min-width:0}}.module-card.hidden{{display:none}}.module-head{{display:flex;justify-content:space-between;gap:12px;align-items:flex-start;margin-bottom:14px}}.module-head h2{{font-size:18px;margin:0 0 4px}}.module-head p{{color:var(--muted);font-size:12px;margin:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:480px}}.module-index{{color:var(--accent);font:700 11px ui-monospace,monospace;margin-right:8px}}.module-count{{color:var(--muted);font-size:11px;white-space:nowrap;border:1px solid var(--line);border-radius:999px;padding:5px 8px}}.list-head{{display:grid;grid-template-columns:minmax(170px,1fr) 60px 72px 72px 62px;gap:8px;color:#68809e;font-size:10px;text-transform:uppercase;letter-spacing:.08em;padding:0 8px 7px 10px}}.ranking-momentum{{display:none}}body.mode-momentum .ranking-composite{{display:none}}body.mode-momentum .ranking-momentum{{display:block}}.rank-item{{display:grid;grid-template-columns:30px minmax(150px,1fr) 58px 70px 68px 58px;gap:8px;align-items:center;border-top:1px solid rgba(36,55,82,.64);padding:11px 8px 11px 0;min-width:0}}.rank-item:first-child{{border-top:0}}.rank-number{{font:700 15px ui-monospace,monospace;color:#7187a4;text-align:center}}.rank-1 .rank-number{{color:#ffd36c}}.rank-2 .rank-number{{color:#c5d6ef}}.rank-3 .rank-number{{color:#cf9e70}}.rank-main{{min-width:0}}.rank-title{{display:flex;align-items:center;gap:7px;min-width:0}}.rank-title a{{font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}.rank-title a:hover{{color:var(--accent)}}.priority{{font-size:9px;padding:2px 5px;border-radius:4px;background:#22334b;color:#9bb1d0;flex:none}}.priority-p0{{background:rgba(73,214,189,.12);color:var(--teal)}}.priority-p1{{background:rgba(115,167,255,.12);color:var(--accent)}}.rank-meta{{display:flex;gap:8px;color:#7187a4;font-size:10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:3px}}.score-track{{height:3px;background:#20314a;border-radius:9px;margin-top:7px;overflow:hidden}}.score-track span{{display:block;height:100%;border-radius:inherit;background:linear-gradient(90deg,var(--accent),var(--teal))}}.rank-metric,.rank-score{{text-align:right;min-width:0}}.rank-metric strong,.rank-score strong{{display:block;font-size:12px;white-space:nowrap}}.rank-metric small,.rank-score small{{display:block;color:#7187a4;font-size:9px;margin-top:2px}}.rank-metric.positive strong{{color:var(--teal)}}.rank-metric.muted strong{{color:#8497b1}}.rank-score strong{{color:var(--orange)}}.empty-state{{color:var(--muted);font-size:12px;padding:17px 8px;border-top:1px solid rgba(36,55,82,.64)}}.watchlist{{margin-top:28px;background:rgba(16,29,49,.72);border:1px solid var(--line);border-radius:18px;padding:20px}}.watch-head{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px}}.watch-head h2{{margin:0;font-size:18px}}.watch-head span{{font-size:12px;color:var(--muted)}}.watch-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}.watch-item{{border:1px solid var(--line);border-radius:10px;padding:10px 12px;background:rgba(20,36,59,.65);min-width:0}}.watch-item:hover{{border-color:var(--accent)}}.watch-item span,.watch-item small{{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.watch-item span{{font-weight:650}}.watch-item small{{color:var(--muted);font-size:10px;margin-top:3px}}footer{{display:flex;justify-content:space-between;gap:16px;color:#7187a4;font-size:11px;margin-top:28px;padding-top:16px;border-top:1px solid var(--line)}}@media(max-width:1050px){{.kpis{{grid-template-columns:repeat(3,1fr)}}.modules{{grid-template-columns:1fr}}}}
@media(max-width:650px){{html{{scroll-padding-top:116px}}body{{overflow-x:hidden}}.shell{{padding:22px 12px 48px}}.topbar{{display:block;margin-bottom:20px}}.eyebrow{{font-size:10px;letter-spacing:.12em}}h1{{font-size:34px;margin-top:7px;letter-spacing:-.035em}}.subtitle{{font-size:13px;line-height:1.65}}.date-pill{{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:16px;min-width:0;padding:10px 12px;text-align:left}}.date-pill strong{{font-size:17px}}.date-pill span{{text-align:right;font-size:10px}}.kpis{{grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;margin-bottom:18px}}.kpi{{padding:13px 14px;border-radius:14px}}.kpi:last-child{{grid-column:1/-1}}.kpi-value{{font-size:23px}}.kpi-hint{{font-size:10px}}.toolbar{{display:block;margin:0 -12px 14px;padding:9px 12px 0;background:rgba(8,17,31,.96);backdrop-filter:blur(12px)}}.segmented{{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}}.segmented button{{width:100%;min-height:40px;padding:8px 10px}}.filters{{flex-wrap:nowrap;gap:8px;overflow-x:auto;margin:9px -12px 0;padding:0 12px 10px;scrollbar-width:none;-webkit-overflow-scrolling:touch}}.filters::-webkit-scrollbar{{display:none}}.filters button{{flex:0 0 auto;min-height:38px;padding:8px 12px}}.toolbar-note{{display:none}}.modules{{gap:12px}}.module-card{{padding:14px 12px;border-radius:16px}}.module-head{{gap:8px;margin-bottom:10px}}.module-head h2{{font-size:17px;line-height:1.3}}.module-head p{{max-width:calc(100vw - 116px);white-space:normal;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}}.module-count{{font-size:10px;padding:4px 7px}}.list-head{{display:none !important}}.rank-item{{grid-template-columns:28px repeat(3,minmax(0,1fr)) 48px;grid-template-rows:auto auto;column-gap:6px;row-gap:11px;padding:14px 0;align-items:start}}.rank-number{{grid-column:1;grid-row:1/span 2;padding-top:1px;font-size:14px}}.rank-main{{grid-column:2/5;grid-row:1}}.rank-score{{grid-column:5;grid-row:1;text-align:right}}.rank-item>.rank-metric:nth-child(3){{grid-column:2;grid-row:2}}.rank-item>.rank-metric:nth-child(4){{grid-column:3;grid-row:2}}.rank-item>.rank-metric:nth-child(5){{grid-column:4;grid-row:2}}.rank-metric{{text-align:left}}.rank-metric strong,.rank-score strong{{font-size:13px}}.rank-metric small,.rank-score small{{font-size:9px}}.rank-meta span:nth-child(2){{display:none}}.rank-title a{{font-size:14px}}.score-track{{margin-top:8px}}.watchlist{{margin-top:18px;padding:15px 12px}}.watch-head{{display:block}}.watch-head span{{display:block;margin-top:3px}}.watch-grid{{grid-template-columns:1fr}}footer{{display:block;margin-top:20px}}footer span{{display:block;margin-top:5px}}}}
@media(max-width:360px){{.shell{{padding-left:9px;padding-right:9px}}.toolbar{{margin-left:-9px;margin-right:-9px;padding-left:9px;padding-right:9px}}.filters{{margin-left:-9px;margin-right:-9px;padding-left:9px;padding-right:9px}}.module-card{{padding-left:10px;padding-right:10px}}.rank-item{{grid-template-columns:25px repeat(3,minmax(0,1fr)) 46px;column-gap:4px}}.rank-metric strong,.rank-score strong{{font-size:12px}}}}
@media(max-width:650px){{.date-pill strong{{white-space:nowrap;flex:none}}}}
</style></head><body><main class="shell">
<header class="topbar"><div><div class="eyebrow">AI Agent Open Source Intelligence</div><h1>Agent 技术开源周榜</h1><p class="subtitle">把 18 个核心技术模块的开源项目放在同一张地图上，用社区热度、周增速和架构相关度看清本周变化。</p></div><div class="date-pill"><strong>{date}</strong><span>{baseline_note}</span></div></header>
<section class="kpis"><div class="kpi"><div class="kpi-label">覆盖模块</div><div class="kpi-value">{module_count}</div><div class="kpi-hint">核心 Agent 技术层</div></div><div class="kpi"><div class="kpi-label">榜单项目</div><div class="kpi-value">{project_count}</div><div class="kpi-hint">人工策展候选池</div></div><div class="kpi"><div class="kpi-label">总 Stars</div><div class="kpi-value">{total_stars}</div><div class="kpi-hint">Top 5 汇总</div></div><div class="kpi"><div class="kpi-label">标准化周增量</div><div class="kpi-value">{total_delta}</div><div class="kpi-hint">按 7 天口径</div></div><div class="kpi"><div class="kpi-label">刷新健康度</div><div class="kpi-value">{health}</div><div class="kpi-hint">{active_count} 个项目近期活跃</div></div></section>
<div class="toolbar"><div class="segmented"><button class="mode-btn active" data-mode="composite">综合榜</button><button class="mode-btn" data-mode="momentum">本周增长榜</button></div><div class="filters"><button class="filter-chip active" data-filter="all">全部模块</button>{module_options}</div><span class="toolbar-note">点击项目名打开 GitHub · 评分条越长越靠前</span></div>
<section class="modules">{module_cards}</section><section class="watchlist"><div class="watch-head"><h2>新发现观察池</h2><span>{discovery_count} 个候选 · 仅作研究线索，不自动进入正式榜单</span></div><div class="watch-grid">{watchlist_html}</div></section>
<footer><span>数据源：GitHub API / 公开仓库页面 · 当前快照 {date}</span><span>排名是研究辅助信号，不代表生产成熟度、许可证结论或采用建议。</span></footer></main>
<script>const body=document.body;document.querySelectorAll('.mode-btn').forEach(btn=>btn.addEventListener('click',()=>{{document.querySelectorAll('.mode-btn').forEach(item=>item.classList.remove('active'));btn.classList.add('active');body.classList.toggle('mode-momentum',btn.dataset.mode==='momentum')}}));document.querySelectorAll('.filter-chip').forEach(btn=>btn.addEventListener('click',()=>{{document.querySelectorAll('.filter-chip').forEach(item=>item.classList.remove('active'));btn.classList.add('active');const filter=btn.dataset.filter;document.querySelectorAll('.module-card').forEach(card=>card.classList.toggle('hidden',filter!=='all'&&card.dataset.module!==filter))}}));</script></body></html>""".format(
        date=_esc(as_of.isoformat()),
        baseline_note=_esc(baseline_note),
        module_count=len(module_config),
        project_count=len(unique_projects),
        total_stars=format_stars(total_stars),
        total_delta=_delta(total_delta, previous_date),
        health=health,
        active_count=active_count,
        module_options=module_options,
        module_cards=module_cards,
        discovery_count=discovery_count,
        watchlist_html=watchlist_html,
    )
