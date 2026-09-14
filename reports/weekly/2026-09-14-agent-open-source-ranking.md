# AI Agent 开源项目周榜（2026-09-14）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-09-07，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 41.6k | +446 | 100 | 87.23 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 29.4k | +181 | 100 | 83.56 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 13.5k | +146 | 100 | 82.06 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.5k | +95 | 100 | 80.99 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 58.5k | +315 | 100 | 78.77 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +446.0 | +1.08% | 77.33 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +181.0 | +0.62% | 71.54 |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | +315.0 | +0.54% | 71.03 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +146.0 | +1.09% | 70.73 |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | +271.0 | +0.98% | 70.50 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1896 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：863 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：6919 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3811 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.
- [GCWing/OpenBitFun](https://github.com/GCWing/OpenBitFun)：2124 Stars；匹配度 2；OpenBitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 23.0k | +135 | 100 | 82.26 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.4k | +24 | 100 | 66.94 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +9 | 100 | 62.53 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +135.0 | +0.59% | 69.80 |
| 2 | [Restate](https://github.com/restatedev/restate) | +24.0 | +0.55% | 55.94 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +9.0 | +0.58% | 50.46 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1242 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7933 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：112 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | 22.7k | +2191 | 100 | 97.42 | 独立 Context Manager 的直接样本 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | 37.1k | +1250 | 100 | 91.77 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 48.9k | +144 | 40 | 74.46 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 35.9k | +84 | 100 | 73.82 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.7k | +29 | 100 | 59.66 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | +2191.0 | +10.69% | 98.71 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | +1250.0 | +3.49% | 86.12 |
| 3 | [Continue](https://github.com/continuedev/continue) | +84.0 | +0.23% | 63.34 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +144.0 | +0.30% | 61.19 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +29.0 | +1.08% | 53.76 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：93816 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78295 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：39782 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：27953 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：26870 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 65.3k | +449 | 100 | 87.64 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 30.7k | +127 | 100 | 82.41 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.7k | +90 | 100 | 81.00 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 11.3k | +101 | 100 | 73.01 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 28.4k | +306 | 100 | 70.48 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +449.0 | +0.69% | 76.97 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +127.0 | +0.42% | 69.39 |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | +306.0 | +1.09% | 67.60 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +90.0 | +0.37% | 67.37 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +101.0 | +0.90% | 64.59 |

#### 新发现观察池

- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：1321 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1216 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1054 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)：687 Stars；匹配度 3；The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：26621 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 90.6k | +480 | 100 | 80.74 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 39.6k | +177 | 100 | 76.34 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.2k | +108 | 100 | 75.16 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.0k | +100 | 100 | 74.36 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.5k | +68 | 100 | 72.71 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +480.0 | +0.53% | 73.52 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +177.0 | +0.45% | 67.60 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +108.0 | +0.21% | 64.87 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +100.0 | +0.28% | 64.30 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +68.0 | +0.26% | 62.06 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38633 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：22949 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：138006 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78295 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：72350 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 286.3k | +3803 | 100 | 91.35 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 176.2k | +1270 | 100 | 90.73 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 94.1k | +1470 | 100 | 83.98 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 25.3k | +203 | 65 | 78.57 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 261.5k | +6436 | 100 | 77.52 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Superpowers](https://github.com/obra/superpowers) | +3803.0 | +1.35% | 82.69 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | +1270.0 | +0.73% | 81.45 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | +1470.0 | +1.59% | 79.37 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +6436.0 | +2.52% | 77.55 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +203.0 | +0.81% | 67.12 |

#### 新发现观察池

- [tt-a1i/archify](https://github.com/tt-a1i/archify)：61137 Stars；匹配度 3；Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.
- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：58663 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：31571 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：138006 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：61981 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [ToolHive](https://github.com/stacklok/toolhive) | 2.2k | +89 | 100 | 80.66 | 企业级 MCP Server 运行治理 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.3k | +69 | 100 | 80.13 | Python 官方 SDK |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.4k | +50 | 100 | 78.27 | TypeScript 官方 SDK |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.2k | +51 | 100 | 77.85 | MCP 规范与文档主仓库 |
| 5 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 90.3k | +182 | 100 | 77.61 | 生态入口不代表每个 Server 均成熟 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [ToolHive](https://github.com/stacklok/toolhive) | +89.0 | +4.29% | 73.05 |
| 2 | [Open Connector](https://github.com/oomol-lab/open-connector) | +144.0 | +2.58% | 69.15 |
| 3 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +182.0 | +0.20% | 67.96 |
| 4 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +69.0 | +0.28% | 65.87 |
| 5 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +51.0 | +0.56% | 64.06 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：94926 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：71950 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57504 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：43151 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：37072 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 15.9k | +121 | 100 | 81.48 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 25.8k | +92 | 100 | 81.13 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.8k | +30 | 100 | 67.32 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +121.0 | +0.77% | 69.28 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +92.0 | +0.36% | 67.50 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +30.0 | +1.07% | 57.70 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：555 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1455 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：671 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：507 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support
- [mahonzhan/awesome-agent-harness](https://github.com/mahonzhan/awesome-agent-harness)：280 Stars；匹配度 2；A curated awesome list of agent harnesses, agent frameworks, workflow frameworks, and emerging agent protocols.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 31.6k | +651 | 100 | 81.36 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.7k | +33 | 100 | 69.89 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.4k | +119 | 20 | 56.42 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +651.0 | +2.11% | 77.29 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +33.0 | +0.19% | 57.99 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +119.0 | +0.17% | 49.79 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21975 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：105485 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：72350 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：48125 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：46961 Stars；匹配度 1；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 15.2k | +167 | 100 | 82.67 | Agent 原生 Sandbox Runtime |
| 2 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 5.2k | +369 | 100 | 82.10 | 无完整容器的 OS 级限制 |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | 13.8k | +96 | 100 | 80.50 | 企业 Agent 云端安全执行环境 |
| 4 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.6k | +76 | 100 | 79.21 | NVIDIA 自主 Agent 安全 Runtime |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 12.2k | +369 | 100 | 79.09 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +369.0 | +7.61% | 83.86 |
| 2 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +369.0 | +3.12% | 75.62 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +167.0 | +1.11% | 71.55 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +96.0 | +0.70% | 67.86 |
| 5 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +76.0 | +0.89% | 66.66 |

#### 新发现观察池

- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2145 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [Augani/dory](https://github.com/Augani/dory)：1577 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1135 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1110 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [Aethena-Lab/Z3r0](https://github.com/Aethena-Lab/Z3r0)：826 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 114.5k | +1745 | 100 | 91.55 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 22.6k | +332 | 100 | 85.72 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 24.3k | +109 | 100 | 81.60 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.6k | +41 | 100 | 69.39 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +15 | 65 | 58.93 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | +1745.0 | +1.55% | 83.09 |
| 2 | [CUA](https://github.com/trycua/cua) | +332.0 | +1.49% | 76.12 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +109.0 | +0.45% | 68.49 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +41.0 | +0.54% | 59.03 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +15.0 | +1.11% | 48.55 |

#### 新发现观察池

- [feder-cr/AIHawk](https://github.com/feder-cr/AIHawk)：30802 Stars；匹配度 3；Anti detect browser and web browsing agent: an open-source MCP server for undetected browsing, AI web scraping and computer use agents. No captchas.
- [microsoft/Webwright](https://github.com/microsoft/Webwright)：5984 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4128 Stars；匹配度 2；Open-source, vision-first browser agent
- [oxylabs/browser-agent-py](https://github.com/oxylabs/browser-agent-py)：1564 Stars；匹配度 2；AI Browser Agent is an advanced Browser AI tool developed by Oxylabs AI Studio that automates real user browsing tasks using natural language instructions.
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1045 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 58.7k | +485 | 100 | 87.82 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 65.8k | +3689 | 100 | 80.21 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.0k | +63 | 40 | 62.48 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.0k | +10 | 85 | 55.23 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3689.0 | +5.94% | 84.01 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +485.0 | +0.83% | 77.55 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +63.0 | +0.49% | 52.52 |
| 4 | [Plano](https://github.com/katanemo/plano) | +10.0 | +0.14% | 45.38 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：8033 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：5216 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5096 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44131 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：17115 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 34.6k | +286 | 100 | 85.37 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.4k | +98 | 100 | 80.40 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 22.0k | +162 | 100 | 75.36 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.8k | +17 | 100 | 65.25 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | +14 | 65 | 60.76 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +286.0 | +0.83% | 74.42 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +98.0 | +0.86% | 68.13 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +162.0 | +0.74% | 67.23 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +17.0 | +0.62% | 54.02 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +14.0 | +0.19% | 47.84 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1536 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：126 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：202 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：143 Stars；匹配度 2；无仓库描述
- [dreadnode/agent-lens](https://github.com/dreadnode/agent-lens)：115 Stars；匹配度 2；Agent observability and replay tooling for AI safety & interpretability research.

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 25.1k | +203 | 100 | 83.81 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 18.3k | +118 | 100 | 81.53 | LLM/Agent Evaluation Framework |
| 3 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.8k | +51 | 100 | 69.89 | 真实代码 Issue 基准 |
| 4 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.8k | +51 | 100 | 69.59 | 可复现评测任务框架 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.8k | +9 | 100 | 64.38 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +203.0 | +0.82% | 72.38 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +118.0 | +0.65% | 69.04 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +51.0 | +1.88% | 61.91 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +51.0 | +0.88% | 60.57 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +9.0 | +0.15% | 50.76 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：372 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：452 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：440 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：329 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：210 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 17.1k | +683 | 100 | 89.99 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.5k | +49 | 100 | 77.04 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.1k | +43 | 100 | 69.47 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 455 | +2 | 20 | 37.26 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +683.0 | +4.16% | 84.85 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +49.0 | +1.11% | 64.34 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +43.0 | +0.61% | 59.34 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +2.0 | +0.44% | 27.27 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：1993 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：562 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：312 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：201 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work
- [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)：3056 Stars；匹配度 2；Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | 5.8k | +46 | 100 | 77.00 | Agent/Skill/Tool/Resource 关系授权 |
| 2 | [Logto](https://github.com/logto-io/logto) | 14.5k | +29 | 100 | 76.70 | AI App 身份认证与授权底座 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.4k | +45 | 100 | 70.53 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | +46.0 | +0.80% | 63.64 |
| 2 | [Logto](https://github.com/logto-io/logto) | +29.0 | +0.20% | 60.96 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +45.0 | +0.31% | 59.59 |

#### 新发现观察池

- [Vorim-AI-Labs/vorim-mcp-server](https://github.com/Vorim-AI-Labs/vorim-mcp-server)：73 Stars；匹配度 3；MCP server for Vorim AI — AI agent identity, permissions, and audit trails. 19 tools for Claude, OpenAI, Cursor, VS Code, and any MCP-compatible client.
- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：63 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8413 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2699 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 37.3k | +121 | 100 | 82.52 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12.1k | +104 | 100 | 73.18 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.5k | +56 | 65 | 65.69 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +121.0 | +0.33% | 69.14 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +104.0 | +0.86% | 64.73 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +56.0 | +0.49% | 55.59 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：796 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 123.9k | +1875 | 100 | 91.54 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenHands](https://github.com/OpenHands/OpenHands) | 87.8k | +1422 | 100 | 91.42 | 软件 Agent 执行与评测 |
| 3 | [OpenCode](https://github.com/anomalyco/opencode) | 207.2k | +1809 | 100 | 90.88 | 终端 Agent 架构参考 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 82.4k | +742 | 100 | 89.71 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 245.2k | +2569 | 100 | 83.56 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [herdr](https://github.com/herdrdev/herdr) | +2398.0 | +6.68% | 85.03 |
| 2 | [OpenHands](https://github.com/OpenHands/OpenHands) | +1422.0 | +1.65% | 83.18 |
| 3 | [Codex](https://github.com/openai/codex) | +1875.0 | +1.54% | 83.07 |
| 4 | [OpenCode](https://github.com/anomalyco/opencode) | +1809.0 | +0.88% | 81.76 |
| 5 | [DeerFlow](https://github.com/bytedance/deer-flow) | +742.0 | +0.91% | 80.14 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：26726 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：257870 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：76700 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：72350 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：46961 Stars；匹配度 2；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
