# AI Agent 核心技术开源研究

这是一套面向 AI Agent 应用架构师的开源技术地图。重点不是罗列所有“能做 Agent”的框架，而是拆解 Agent 系统的核心技术层，识别每层最值得研究的开源实现。

在线版本：[AI Agent 技术开源周榜](https://yuxiaoyi24.github.io/ai-agent-open-source-ranking/)

## 研究入口

- [Agent 核心技术开源全景（2026）](./agent-core-open-source-landscape-2026.md)：模块地图、核心项目、源码研究问题和 12 周路线。
- [项目清单](./data/agent-open-source-projects.csv)：可按模块、优先级、Stars、License 和项目类型筛选。
- [可视化周榜](./reports/weekly/latest.html)：用模块卡片、评分条和交互切换查看每个模块的 Top 5。
- [每周动态榜单（Markdown）](./reports/weekly/latest.md)：每个模块的综合 Top 5、本周增长 Top 5 和新发现观察池。
- [周榜工具说明](./docs/weekly-ranking-tool.md)：评分模型、运行命令、历史快照和自动化维护方式。

## 当前范围

当前版本覆盖 18 个模块、105 个主流或新兴项目：Runtime、Durable Execution、Context、Memory、Knowledge/RAG、Skills、MCP、Agent 协议、多 Agent、Sandbox、Browser/Computer Use、Model Gateway、Observability、Evaluation、Security、Identity、HITL/UI，以及 Coding Agent Harness / 完整平台。

## 数据说明

- Stars 为 2026-08-05 快照，只代表社区传播度，不等于生产成熟度。
- P0/P1/P2 根据架构代表性、生态采用、近期活跃度和与你现有 AI Stack 的相关性综合判断，不按 Stars 机械排序。
- GitHub API、公开仓库页面和本地截至 2026-08-02 的发布记录交叉核验；许可证为 `需复核` 时，不应直接用于企业引入决策。
- 同一项目可能覆盖多个模块，CSV 只设置一个主模块，其他能力放在 `tags` 中。

## 每周刷新

```bash
python3 scripts/update_agent_landscape.py --discover
```

脚本会同时生成 `reports/weekly/latest.html`、日期版 HTML、Markdown 和 JSON；HTML 不依赖外部前端框架，直接用浏览器打开即可。

提供只读 `GITHUB_TOKEN` 时使用 GitHub GraphQL 批量刷新；没有 Token 时自动回退到公开仓库页面与 commit feed。新发现项目只进入观察池，不会自动改写人工策展清单。

## 在线发布

`.github/workflows/publish.yml` 负责 GitHub Pages 发布：推送到 `main` 时发布现有 HTML；每周一 09:00（Asia/Shanghai）自动刷新 GitHub 数据、运行测试、保存历史快照并发布新版页面。也可以在 GitHub Actions 中手动触发刷新。
