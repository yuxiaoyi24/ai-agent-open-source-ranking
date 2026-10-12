# AI Agent 开源项目周榜（2026-10-12）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-10-05，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 43.1k | +376 | 100 | 86.59 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 30.0k | +139 | 100 | 82.68 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 14.1k | +121 | 100 | 81.37 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.8k | +74 | 100 | 80.19 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 59.6k | +231 | 100 | 77.76 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +376.0 | +0.88% | 76.09 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +139.0 | +0.47% | 69.92 |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +121.0 | +0.87% | 69.37 |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | +231.0 | +0.39% | 69.18 |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | +162.0 | +0.57% | 67.11 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1900 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：876 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：6997 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4454 Stars；匹配度 2；agent runtime security - zero trust, zero setup, zero latency agent sandbox
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3820 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 23.6k | +147 | 100 | 82.59 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.5k | +27 | 100 | 67.38 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +13 | 100 | 63.79 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +147.0 | +0.63% | 70.32 |
| 2 | [Restate](https://github.com/restatedev/restate) | +27.0 | +0.60% | 56.64 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +13.0 | +0.81% | 52.66 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1249 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：8103 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：133 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | 26.7k | +1303 | 100 | 92.83 | 独立 Context Manager 的直接样本 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | 39.7k | +487 | 100 | 87.56 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 3 | [Continue](https://github.com/continuedev/continue) | 36.2k | +75 | 100 | 73.48 | IDE 场景上下文装配 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | 49.5k | +98 | 40 | 73.28 | 代码图和 token 预算的成熟实现 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.8k | +23 | 100 | 58.82 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | +1303.0 | +5.12% | 89.10 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | +487.0 | +1.24% | 78.05 |
| 3 | [Continue](https://github.com/continuedev/continue) | +75.0 | +0.21% | 62.73 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +98.0 | +0.20% | 59.07 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +23.0 | +0.83% | 52.15 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：99828 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79060 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：40233 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：28464 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：27399 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Cognee](https://github.com/topoteretes/cognee) | 32.1k | +705 | 100 | 89.26 | 知识图谱驱动长期记忆 |
| 2 | [Mem0](https://github.com/mem0ai/mem0) | 67.0k | +433 | 100 | 87.54 | 通用 Agent Memory Layer |
| 3 | [Letta](https://github.com/letta-ai/letta) | 25.1k | +86 | 65 | 75.62 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 11.8k | +125 | 100 | 73.86 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 29.3k | +191 | 100 | 68.75 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Cognee](https://github.com/topoteretes/cognee) | +705.0 | +2.25% | 81.74 |
| 2 | [Mem0](https://github.com/mem0ai/mem0) | +433.0 | +0.65% | 76.72 |
| 3 | [MemOS](https://github.com/MemTensor/MemOS) | +125.0 | +1.07% | 66.04 |
| 4 | [agentmemory](https://github.com/rohitg00/agentmemory) | +191.0 | +0.66% | 64.38 |
| 5 | [Letta](https://github.com/letta-ai/letta) | +86.0 | +0.34% | 61.86 |

#### 新发现观察池

- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：3401 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1269 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1101 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：48545 Stars；匹配度 2；Hindsight: Agent Memory That Learns
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：27938 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 92.0k | +341 | 100 | 79.62 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 40.1k | +95 | 100 | 74.36 | 轻量图 RAG 和增量更新 |
| 3 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.3k | +69 | 100 | 73.23 | 图谱社区摘要与检索 |
| 4 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.5k | +53 | 100 | 73.03 | 文档和数据 Agent 基础栈 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.7k | +70 | 100 | 72.81 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +341.0 | +0.37% | 71.49 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +95.0 | +0.24% | 64.06 |
| 3 | [GraphRAG](https://github.com/microsoft/graphrag) | +69.0 | +0.19% | 62.28 |
| 4 | [Haystack](https://github.com/deepset-ai/haystack) | +70.0 | +0.26% | 62.23 |
| 5 | [LlamaIndex](https://github.com/run-llama/llama_index) | +53.0 | +0.10% | 61.10 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38681 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：33329 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：141322 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79060 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：75089 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 297.9k | +2495 | 100 | 90.84 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 180.6k | +897 | 100 | 90.19 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 105.2k | +3893 | 100 | 86.34 | 生产级编码 Skill 样本 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | 286.7k | +10326 | 100 | 78.74 | 高传播度内容样本不等于 Runtime |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 26.1k | +141 | 65 | 77.31 | Skill 可移植规范 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [agent-skills](https://github.com/addyosmani/agent-skills) | +3893.0 | +3.84% | 83.94 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | +2495.0 | +0.84% | 81.69 |
| 3 | [Anthropic Skills](https://github.com/anthropics/skills) | +897.0 | +0.50% | 80.45 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +10326.0 | +3.74% | 79.97 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +141.0 | +0.54% | 64.78 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：67136 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：33866 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：141322 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [tt-a1i/archify](https://github.com/tt-a1i/archify)：82213 Stars；匹配度 2；Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：64001 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.5k | +62 | 100 | 79.81 | Python 官方 SDK |
| 2 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.4k | +48 | 100 | 77.68 | MCP 规范与文档主仓库 |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.6k | +39 | 100 | 77.50 | TypeScript 官方 SDK |
| 4 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 91.2k | +147 | 100 | 76.97 | 生态入口不代表每个 Server 均成熟 |
| 5 | [ToolHive](https://github.com/stacklok/toolhive) | 2.3k | +35 | 100 | 75.37 | 企业级 MCP Server 运行治理 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +147.0 | +0.16% | 66.81 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +62.0 | +0.25% | 65.28 |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +48.0 | +0.51% | 63.69 |
| 4 | [ToolHive](https://github.com/stacklok/toolhive) | +35.0 | +1.57% | 63.00 |
| 5 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +39.0 | +0.29% | 62.53 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：96153 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：75089 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57567 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：46392 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：38038 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 16.5k | +148 | 100 | 82.26 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 26.1k | +102 | 100 | 81.48 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.9k | +45 | 85 | 66.76 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +148.0 | +0.91% | 70.60 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +102.0 | +0.39% | 68.10 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +45.0 | +1.55% | 58.44 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：552 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [openJiuwen-ai/agent-protocol](https://github.com/openJiuwen-ai/agent-protocol)：113 Stars；匹配度 3；openJiuwen agent-protocol provides implementations of agent communication protocols, including C++ SDKs for MCP and A2A protocols.
- [BrightbeamAI/chap](https://github.com/BrightbeamAI/chap)：107 Stars；匹配度 3；CHAP, the Collaborative Human Agent Protocol, is a MCP/A2A-compatible runtime for auditable human-agent work: approvals, overrides, handoffs, escalation and verifiable evidence logs.
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1458 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：684 Stars；匹配度 2；无仓库描述

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 33.1k | +342 | 100 | 78.53 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.9k | +61 | 100 | 71.80 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.8k | +63 | 20 | 54.53 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +342.0 | +1.04% | 71.96 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +61.0 | +0.34% | 61.35 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +63.0 | +0.09% | 46.45 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：22048 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：110703 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：74376 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：48965 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47353 Stars；匹配度 1；Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 15.9k | +984 | 100 | 93.36 | NVIDIA 自主 Agent 安全 Runtime |
| 2 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 5.5k | +662 | 100 | 86.28 | 无完整容器的 OS 级限制 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 15.8k | +119 | 100 | 81.41 | Agent 原生 Sandbox Runtime |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | 14.3k | +113 | 100 | 81.13 | 企业 Agent 云端安全执行环境 |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 12.9k | +79 | 100 | 72.24 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +662.0 | +13.65% | 91.65 |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +984.0 | +6.60% | 91.53 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +119.0 | +0.76% | 69.17 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +113.0 | +0.80% | 68.90 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +83.0 | +2.00% | 64.96 |

#### 新发现观察池

- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4454 Stars；匹配度 3；agent runtime security - zero trust, zero setup, zero latency agent sandbox
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2278 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [Augani/dory](https://github.com/Augani/dory)：1603 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1501 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1181 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CUA](https://github.com/trycua/cua) | 29.4k | +1337 | 100 | 92.64 | Computer Use 驱动和训练评测平台 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | 117.7k | +520 | 100 | 88.56 | 浏览器 Agent 主流实现 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 25.6k | +94 | 100 | 81.19 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.8k | +47 | 100 | 69.88 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +14 | 100 | 63.94 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CUA](https://github.com/trycua/cua) | +1337.0 | +4.76% | 88.46 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | +520.0 | +0.44% | 77.58 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +94.0 | +0.37% | 67.63 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +47.0 | +0.61% | 59.86 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +14.0 | +1.01% | 53.28 |

#### 新发现观察池

- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4134 Stars；匹配度 2；Open-source, vision-first browser agent
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1367 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1008 Stars；匹配度 2；Build browser agents for real world tasks
- [LvcidPsyche/auto-browser](https://github.com/LvcidPsyche/auto-browser)：902 Stars；匹配度 2；Give your AI agent a real browser — with a human in the loop. Open-source MCP-native browser agent.
- [tiliondev/fortress](https://github.com/tiliondev/fortress)：748 Stars；匹配度 2；Stealth Chromium engine that stops scrapers and browser agents from getting blocked, with one line of code change.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 61.0k | +866 | 100 | 90.17 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 75.4k | +2350 | 100 | 77.73 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.2k | +44 | 40 | 61.34 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.1k | +6 | 100 | 56.12 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | +866.0 | +1.44% | 81.73 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2350.0 | +3.22% | 78.69 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +44.0 | +0.34% | 50.45 |
| 4 | [Plano](https://github.com/katanemo/plano) | +6.0 | +0.08% | 45.23 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：8713 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [TykTechnologies/tyk](https://github.com/TykTechnologies/tyk)：10857 Stars；匹配度 2；Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol)
- [looplj/axonhub](https://github.com/looplj/axonhub)：5349 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5207 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44262 Stars；匹配度 1；🦍 The API and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 35.7k | +291 | 100 | 85.47 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.8k | +89 | 100 | 80.08 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 22.5k | +143 | 100 | 74.94 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.8k | +24 | 100 | 66.49 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.5k | +14 | 100 | 66.02 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +291.0 | +0.82% | 74.51 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +89.0 | +0.76% | 67.46 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +143.0 | +0.64% | 66.41 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +24.0 | +0.85% | 56.17 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +14.0 | +0.19% | 53.09 |

#### 新发现观察池

- [langwatch/langwatch](https://github.com/langwatch/langwatch)：4937 Stars；匹配度 3；Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company.
- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1545 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：126 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：192 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：145 Stars；匹配度 2；无仓库描述

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 25.9k | +202 | 100 | 83.82 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 18.8k | +120 | 100 | 81.62 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 3.0k | +52 | 100 | 69.67 | 可复现评测任务框架 |
| 4 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.9k | +27 | 100 | 67.69 | Agent Evaluation 与 Testing |
| 5 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 6.0k | +33 | 85 | 66.13 | 真实代码 Issue 基准 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +202.0 | +0.79% | 72.32 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +120.0 | +0.64% | 69.13 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +52.0 | +1.77% | 61.86 |
| 4 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +27.0 | +0.46% | 56.59 |
| 5 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +33.0 | +0.55% | 55.53 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：376 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：560 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：452 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：331 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：211 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 20.0k | +579 | 100 | 88.61 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.6k | +28 | 100 | 75.01 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.3k | +31 | 100 | 68.41 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 469 | +2 | 20 | 37.30 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +579.0 | +2.98% | 81.81 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +28.0 | +0.61% | 60.61 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +31.0 | +0.43% | 57.39 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +2.0 | +0.43% | 27.27 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：2019 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：580 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)：410 Stars；匹配度 3；Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents. Executable, testable rules for prompt injection, tool poisoning, context exfiltration and MCP attacks. Merged into open-source projects at Microsoft, Cisco, Gen Digital, MISP and FINOS. MIT-licensed.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：337 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：202 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | 6.0k | +33 | 100 | 75.87 | Agent/Skill/Tool/Resource 关系授权 |
| 2 | [Logto](https://github.com/logto-io/logto) | 14.7k | +21 | 100 | 75.76 | AI App 身份认证与授权底座 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.5k | +37 | 100 | 69.94 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | +33.0 | +0.56% | 61.53 |
| 2 | [Logto](https://github.com/logto-io/logto) | +21.0 | +0.14% | 59.28 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +37.0 | +0.26% | 58.52 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：67 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8408 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2695 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [VibeTensor/attestix](https://github.com/VibeTensor/attestix)：874 Stars；匹配度 2；Attestix - Attestation Infrastructure for AI Agents. DID-based agent identity, W3C Verifiable Credentials, EU AI Act compliance layer, delegation chains, and reputation scoring. 47 MCP tools across 9 modules.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38.0k | +201 | 100 | 84.22 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12.5k | +82 | 100 | 72.34 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.7k | +34 | 40 | 60.36 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +201.0 | +0.53% | 72.12 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +82.0 | +0.66% | 63.15 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +34.0 | +0.29% | 48.98 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：793 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | 212.8k | +997 | 100 | 90.46 | 终端 Agent 架构参考 |
| 2 | [Codex](https://github.com/openai/codex) | 128.7k | +838 | 100 | 90.15 | 完整 Coding Agent Harness 源码样本 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 90.6k | +635 | 100 | 89.22 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 83.7k | +325 | 100 | 86.84 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 252.9k | +1611 | 100 | 83.14 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | +997.0 | +0.47% | 80.93 |
| 2 | [Codex](https://github.com/openai/codex) | +838.0 | +0.66% | 80.42 |
| 3 | [Paperclip](https://github.com/paperclipai/paperclip) | +3226.0 | +3.32% | 79.13 |
| 4 | [OpenHands](https://github.com/OpenHands/OpenHands) | +635.0 | +0.71% | 79.03 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +1611.0 | +0.64% | 77.53 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：27320 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [1jehuang/jcode](https://github.com/1jehuang/jcode)：20519 Stars；匹配度 3；High performance coding agent harness written in rust
- [zai-org/ZCode](https://github.com/zai-org/ZCode)：7697 Stars；匹配度 3；Z.ai's coding agent harness. Powerful, intelligent, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：277387 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：78393 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
