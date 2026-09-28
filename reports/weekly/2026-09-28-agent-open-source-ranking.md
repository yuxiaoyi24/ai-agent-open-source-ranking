# AI Agent 开源项目周榜（2026-09-28）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-09-21，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Strands Harness SDK](https://github.com/strands-agents/harness-sdk) | 8.5k | +1114 | 100 | 88.22 | 原 sdk-python 已重定向到 harness-sdk |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 42.4k | +344 | 100 | 86.25 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 13.8k | +195 | 100 | 83.28 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 29.7k | +143 | 100 | 82.77 | 用最小抽象观察 Agent loop 和 handoff |
| 5 | [Google ADK Python](https://github.com/google/adk-python) | 21.7k | +85 | 100 | 80.63 | 企业 Agent 生命周期覆盖完整 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Strands Harness SDK](https://github.com/strands-agents/harness-sdk) | +1114.0 | +15.09% | 94.11 |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | +344.0 | +0.82% | 75.50 |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +195.0 | +1.43% | 72.88 |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | +276.0 | +0.47% | 70.23 |
| 5 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +143.0 | +0.48% | 70.09 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1895 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：873 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：6960 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4245 Stars；匹配度 2；agent runtime security - zero trust, zero setup, zero latency.
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3814 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 23.3k | +128 | 100 | 82.09 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.5k | +28 | 100 | 67.48 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +14 | 100 | 64.04 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +128.0 | +0.55% | 69.46 |
| 2 | [Restate](https://github.com/restatedev/restate) | +28.0 | +0.63% | 56.87 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +14.0 | +0.89% | 53.15 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1247 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：8015 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：124 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 38.8k | +582 | 100 | 88.32 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 24.1k | +356 | 100 | 86.05 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 49.2k | +135 | 40 | 74.27 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 36.0k | +86 | 100 | 73.90 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.8k | +22 | 100 | 58.65 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | +582.0 | +1.52% | 79.49 |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | +356.0 | +1.50% | 76.54 |
| 3 | [Continue](https://github.com/continuedev/continue) | +86.0 | +0.24% | 63.47 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +135.0 | +0.28% | 60.83 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +22.0 | +0.80% | 51.88 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：94813 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78680 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：39977 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：28197 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：27161 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 66.1k | +412 | 100 | 87.35 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 31.1k | +224 | 100 | 84.38 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.9k | +110 | 85 | 79.42 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 11.6k | +119 | 100 | 73.66 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 29.0k | +299 | 100 | 70.40 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +412.0 | +0.63% | 76.41 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +224.0 | +0.73% | 72.88 |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | +299.0 | +1.04% | 67.41 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +110.0 | +0.44% | 66.29 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +119.0 | +1.04% | 65.71 |

#### 新发现观察池

- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：1386 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1246 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1078 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：38228 Stars；匹配度 2；Hindsight: Agent Memory That Learns
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：27371 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 91.4k | +322 | 100 | 79.43 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 39.9k | +106 | 100 | 74.70 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.3k | +81 | 100 | 74.29 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.1k | +86 | 100 | 73.90 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.6k | +54 | 100 | 72.01 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +322.0 | +0.35% | 71.15 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +106.0 | +0.27% | 64.66 |
| 3 | [GraphRAG](https://github.com/microsoft/graphrag) | +86.0 | +0.24% | 63.47 |
| 4 | [LlamaIndex](https://github.com/run-llama/llama_index) | +81.0 | +0.15% | 63.33 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +54.0 | +0.20% | 60.81 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38667 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：30725 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：140014 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78680 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：73971 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 292.2k | +2866 | 100 | 90.99 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 178.7k | +1335 | 100 | 90.75 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 99.5k | +1738 | 100 | 84.27 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 25.7k | +198 | 65 | 78.49 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 270.8k | +4230 | 100 | 76.59 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Superpowers](https://github.com/obra/superpowers) | +2866.0 | +0.99% | 81.98 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | +1335.0 | +0.75% | 81.51 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | +1738.0 | +1.78% | 79.80 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +4230.0 | +1.59% | 75.67 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +198.0 | +0.78% | 66.94 |

#### 新发现观察池

- [tt-a1i/archify](https://github.com/tt-a1i/archify)：72989 Stars；匹配度 3；Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.
- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：61604 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：32642 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：140014 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：63053 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.4k | +69 | 100 | 80.14 | Python 官方 SDK |
| 2 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.3k | +58 | 100 | 78.31 | MCP 规范与文档主仓库 |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.5k | +43 | 100 | 77.80 | TypeScript 官方 SDK |
| 4 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 90.6k | +130 | 100 | 76.59 | 生态入口不代表每个 Server 均成熟 |
| 5 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.5k | +33 | 100 | 75.57 | 企业工具网关和统一治理 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +130.0 | +0.14% | 66.15 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +69.0 | +0.28% | 65.87 |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +58.0 | +0.63% | 64.85 |
| 4 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +43.0 | +0.32% | 63.07 |
| 5 | [Open Connector](https://github.com/oomol-lab/open-connector) | +62.0 | +1.06% | 61.91 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：95610 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：73971 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57548 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：45119 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：37636 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 16.1k | +110 | 100 | 81.15 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 26.0k | +80 | 100 | 80.69 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.9k | +15 | 100 | 64.89 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +110.0 | +0.69% | 68.65 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +80.0 | +0.31% | 66.71 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +15.0 | +0.52% | 53.26 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：554 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [BrightbeamAI/chap](https://github.com/BrightbeamAI/chap)：104 Stars；匹配度 3；CHAP, the Collaborative Human Agent Protocol, is a MCP/A2A-compatible runtime for auditable human-agent work: approvals, overrides, handoffs, escalation and verifiable evidence logs.
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1455 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：679 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：508 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 32.5k | +400 | 100 | 79.15 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.8k | +39 | 100 | 70.40 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.7k | +131 | 20 | 56.72 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +400.0 | +1.25% | 73.14 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +39.0 | +0.22% | 58.88 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +131.0 | +0.19% | 50.31 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：22018 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：108946 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：73412 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：48625 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47148 Stars；匹配度 1；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 5.4k | +517 | 100 | 85.52 | 无完整容器的 OS 级限制 |
| 2 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 15.5k | +110 | 100 | 81.11 | Agent 原生 Sandbox Runtime |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | 14.0k | +104 | 100 | 80.81 | 企业 Agent 云端安全执行环境 |
| 4 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.8k | +98 | 100 | 80.21 | NVIDIA 自主 Agent 安全 Runtime |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 12.7k | +99 | 100 | 73.04 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +517.0 | +10.66% | 90.38 |
| 2 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +110.0 | +0.71% | 68.67 |
| 3 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +98.0 | +1.12% | 68.42 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +104.0 | +0.75% | 68.37 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +83.0 | +2.09% | 65.10 |

#### 新发现观察池

- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2195 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [Augani/dory](https://github.com/Augani/dory)：1596 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1309 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1150 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [Aethena-Lab/Z3r0](https://github.com/Aethena-Lab/Z3r0)：910 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CUA](https://github.com/trycua/cua) | 26.7k | +1400 | 100 | 93.24 | Computer Use 驱动和训练评测平台 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | 116.5k | +936 | 100 | 90.62 | 浏览器 Agent 主流实现 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 25.4k | +735 | 100 | 89.71 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.7k | +30 | 100 | 68.38 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +5 | 100 | 60.61 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CUA](https://github.com/trycua/cua) | +1400.0 | +5.53% | 89.92 |
| 2 | [Stagehand](https://github.com/browserbase/stagehand) | +735.0 | +2.98% | 83.21 |
| 3 | [Browser-use](https://github.com/browser-use/browser-use) | +936.0 | +0.81% | 81.29 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +30.0 | +0.39% | 57.20 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +5.0 | +0.36% | 47.34 |

#### 新发现观察池

- [microsoft/Webwright](https://github.com/microsoft/Webwright)：6021 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4131 Stars；匹配度 2；Open-source, vision-first browser agent
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1123 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1006 Stars；匹配度 2；Build browser agents for real world tasks
- [LvcidPsyche/auto-browser](https://github.com/LvcidPsyche/auto-browser)：816 Stars；匹配度 2；Give your AI agent a real browser — with a human in the loop. Open-source MCP-native browser agent.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 59.8k | +478 | 100 | 87.78 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 70.8k | +2175 | 100 | 77.57 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.1k | +50 | 40 | 61.74 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.1k | +7 | 100 | 56.52 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2175.0 | +3.17% | 78.54 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +478.0 | +0.81% | 77.44 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +50.0 | +0.38% | 51.17 |
| 4 | [Plano](https://github.com/katanemo/plano) | +7.0 | +0.10% | 45.93 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：8406 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [TykTechnologies/tyk](https://github.com/TykTechnologies/tyk)：10838 Stars；匹配度 2；Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol)
- [looplj/axonhub](https://github.com/looplj/axonhub)：5316 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5166 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44204 Stars；匹配度 1；🦍 The API and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 35.1k | +255 | 100 | 84.97 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.6k | +83 | 100 | 79.81 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 22.3k | +92 | 100 | 73.43 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.8k | +25 | 100 | 66.62 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.5k | +14 | 100 | 66.02 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +255.0 | +0.73% | 73.65 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +83.0 | +0.72% | 67.02 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +92.0 | +0.41% | 63.74 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +25.0 | +0.90% | 56.45 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +14.0 | +0.19% | 53.09 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1543 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：127 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：195 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：145 Stars；匹配度 2；无仓库描述
- [grafana/agento11y](https://github.com/grafana/agento11y)：124 Stars；匹配度 2；Actually Useful Agent Observability

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 25.5k | +193 | 100 | 83.64 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 18.5k | +116 | 100 | 81.49 | LLM/Agent Evaluation Framework |
| 3 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.9k | +48 | 100 | 69.68 | 真实代码 Issue 基准 |
| 4 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.9k | +49 | 100 | 69.40 | 可复现评测任务框架 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.8k | +9 | 100 | 64.39 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +193.0 | +0.76% | 72.03 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +116.0 | +0.63% | 68.93 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +49.0 | +1.74% | 61.46 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +48.0 | +0.82% | 60.15 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +9.0 | +0.15% | 50.76 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：375 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：522 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：452 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：330 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：211 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 18.5k | +526 | 100 | 88.14 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.6k | +33 | 100 | 75.57 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.2k | +33 | 100 | 68.60 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 464 | +5 | 20 | 39.95 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +526.0 | +2.93% | 81.15 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +33.0 | +0.73% | 61.64 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +33.0 | +0.46% | 57.75 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +5.0 | +1.09% | 32.09 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：2008 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：577 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)：402 Stars；匹配度 3；Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents. Executable, testable rules for prompt injection, tool poisoning, context exfiltration and MCP attacks. Merged into open-source projects at Microsoft, Cisco, Gen Digital, MISP and FINOS. MIT-licensed.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：328 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：202 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | 5.9k | +67 | 100 | 78.45 | Agent/Skill/Tool/Resource 关系授权 |
| 2 | [Logto](https://github.com/logto-io/logto) | 14.6k | +34 | 100 | 77.19 | AI App 身份认证与授权底座 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.5k | +33 | 100 | 69.58 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | +67.0 | +1.15% | 66.22 |
| 2 | [Logto](https://github.com/logto-io/logto) | +34.0 | +0.23% | 61.81 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +33.0 | +0.23% | 57.90 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：67 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [Vorim-AI-Labs/vorim-mcp-server](https://github.com/Vorim-AI-Labs/vorim-mcp-server)：66 Stars；匹配度 3；MCP server for Vorim AI — AI agent identity, permissions, and audit trails. 19 tools for Claude, OpenAI, Cursor, VS Code, and any MCP-compatible client.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8410 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2693 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 37.6k | +131 | 100 | 82.79 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12.3k | +102 | 100 | 73.12 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.6k | +23 | 40 | 59.16 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +131.0 | +0.35% | 69.59 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +102.0 | +0.83% | 64.58 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +23.0 | +0.20% | 46.88 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：797 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：153 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 126.8k | +1253 | 100 | 91.00 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | 210.5k | +1529 | 100 | 90.73 | 终端 Agent 架构参考 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 89.3k | +656 | 100 | 89.33 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 83.1k | +332 | 100 | 86.90 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Paperclip](https://github.com/paperclipai/paperclip) | 90.6k | +9480 | 100 | 84.83 | 工作场景 Agent 管理控制面 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Paperclip](https://github.com/paperclipai/paperclip) | +9480.0 | +11.68% | 92.41 |
| 2 | [Codex](https://github.com/openai/codex) | +1253.0 | +1.00% | 82.00 |
| 3 | [OpenCode](https://github.com/anomalyco/opencode) | +1529.0 | +0.73% | 81.46 |
| 4 | [OpenHands](https://github.com/OpenHands/OpenHands) | +656.0 | +0.74% | 79.25 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +2025.0 | +0.82% | 77.89 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：27132 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：268536 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：77695 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：73412 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47148 Stars；匹配度 2；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
