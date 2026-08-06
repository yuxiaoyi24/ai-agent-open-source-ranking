# AI Agent 开源项目周榜工具

## 1. 目标

工具每周完成五件事：

1. 刷新人工策展候选池中所有 GitHub 仓库的 Stars、提交时间、HEAD、归档状态和许可证。
2. 保存日期快照，与上一期计算 Stars 增量、标准化周增量和周增速。
3. 按 18 个模块生成“综合 Top 5”和“本周增长 Top 5”。
4. 用模块查询发现新仓库，但只放入观察池，不自动污染正式榜单。
5. 生成一个可直接打开的自包含 HTML 仪表盘，提供综合榜/增长榜切换和模块筛选。

## 2. 为什么不是直接搜 GitHub Top 5

GitHub 搜索会把 README 中碰巧出现 Agent、Memory、MCP 的无关项目一起返回。纯 Stars 排名还会产生三个问题：

- 历史大项目长期霸榜，看不到新项目的增量。
- Skills、完整应用、底层基础设施的 Stars 不能直接横比。
- 热度不能反映状态恢复、权限、隔离、评测等架构价值。

因此系统保留两层数据：

- `data/agent-open-source-projects.csv`：人工确认的正式候选池。
- 周报中的“新发现观察池”：自动搜索结果，人工确认后再加入 CSV。

## 3. 排名口径

### 综合榜

有历史快照时：

| 维度 | 权重 |
|---|---:|
| 架构相关度 | 30% |
| 基础热度 | 20% |
| 标准化周 Stars 增量 | 20% |
| 周增速 | 10% |
| 提交活跃度 | 15% |
| 仓库健康度 | 5% |

首期没有历史快照时，临时使用：架构相关度 40%、基础热度 35%、活跃度 20%、健康度 5%。

### 增长榜

周 Stars 增量 35%、周增速 20%、架构相关度 15%、基础热度 10%、活跃度 15%、健康度 5%。

增长榜只展示标准化周 Stars 增量大于 0 的项目；没有正向增量时明确显示空榜，不用历史热度补位。

P0/P1/P2 是人工维护的架构相关度入口，不由脚本根据 Stars 自动修改。具体权重在 `config/ranking.json` 中配置。

## 4. 数据获取

### 推荐：GitHub GraphQL

在环境中提供只读 `GITHUB_TOKEN` 后，脚本会批量查询 GraphQL，获取完整元数据。不要把 Token 写进仓库、配置文件或自动化 Prompt。

```bash
export GITHUB_TOKEN="从密码管理器安全注入的只读 Token"
python3 scripts/update_agent_landscape.py --discover
```

公开仓库只读查询不需要额外仓库写权限。Token 应采用最小权限，并由 Codex 本地执行环境或密码管理器注入。

### 无 Token 回退

没有 `GITHUB_TOKEN` 时，脚本会读取公开 GitHub 仓库页面和 commit Atom feed：

```bash
python3 scripts/update_agent_landscape.py
```

这个模式能刷新 Stars、最新提交和 HEAD，但许可证沿用人工候选池；自动发现使用公开 Search API，18 个模块需要主动节流，运行时间会更长。

公开页面或 feed 出现超时、连接中断、`5xx` 时会自动重试三次；单个仓库最终失败不会中断整期任务，而是保留基线/上一期数据并进入报告风险区。

## 5. 常用命令

```bash
# 离线生成首期报告，用于检查格式
python3 scripts/update_agent_landscape.py --provider offline

# 在线刷新全部 105 个项目
python3 scripts/update_agent_landscape.py

# 在线刷新并发现新候选
python3 scripts/update_agent_landscape.py --discover

# 只检查一个模块，不写入历史
python3 scripts/update_agent_landscape.py --module "Agent Memory" --dry-run

# 运行测试
python3 -m unittest discover -s tests -v
```

局部 `--module` 刷新必须搭配 `--dry-run`，防止不完整快照覆盖正式历史。

## 6. 生成文件

```text
data/
├── agent-open-source-projects.csv    # 人工策展候选池
├── snapshots/YYYY-MM-DD.json         # GitHub 原始周快照
└── rankings/YYYY-MM-DD.json          # 排名、增量、分项得分和观察池

reports/weekly/
├── YYYY-MM-DD-agent-open-source-ranking.md
├── YYYY-MM-DD-agent-open-source-ranking.html
├── latest.md
└── latest.html
```

快照必须保留，下一期依赖它计算增量。不要只保留 `latest.md`。

`latest.html` 是面向研究和汇报的主入口：顶部 KPI 展示覆盖模块、榜单项目、Top 5 汇总 Stars、周增量和刷新健康度；中部模块卡片支持“综合榜 / 本周增长榜”和模块过滤；底部保留自动发现观察池。页面内的评分条是相对分数可视化，不是百分比概率。

## 7. 每周人工复核

自动化完成后，建议只花 20—30 分钟做三项复核：

1. 查看各模块增长榜前两名的 release 和核心提交，补充“为什么上涨”。
2. 检查观察池候选的模块边界、代码成熟度、维护者和 License，决定是否加入 CSV。
3. 对归档、改名、长期无提交或许可证变化项目，调整优先级或移出候选池。

## 8. 自动化建议

建议每周一 09:00（Asia/Shanghai）执行：

```bash
python3 scripts/update_agent_landscape.py --discover
python3 -m unittest discover -s tests -v
```

自动化最后应汇报：最新报告路径、刷新成功/失败数、每个模块增长第一名、观察池新增项目，以及需要人工复核的 License/归档/仓库迁移风险。
