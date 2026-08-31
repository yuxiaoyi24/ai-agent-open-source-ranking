# AI Agent 开源项目周榜（2026-08-31）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-08-24，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 40.7k | +442 | 100 | 87.18 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 29.1k | +186 | 100 | 83.64 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 13.2k | +168 | 100 | 82.63 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.3k | +99 | 100 | 81.12 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 57.8k | +325 | 100 | 78.87 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +442.0 | +1.10% | 77.29 |
| 2 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +168.0 | +1.29% | 71.81 |
| 3 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +186.0 | +0.64% | 71.72 |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | +325.0 | +0.56% | 71.23 |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | +192.0 | +0.70% | 68.20 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1899 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：861 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3796 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.
- [google/ax](https://github.com/google/ax)：1975 Stars；匹配度 2；An open source distributed agent runtime
- [GCWing/BitFun](https://github.com/GCWing/BitFun)：1875 Stars；匹配度 2；BitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 22.6k | +136 | 100 | 82.27 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.4k | +21 | 100 | 66.49 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +7 | 100 | 61.74 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +136.0 | +0.60% | 69.85 |
| 2 | [Restate](https://github.com/restatedev/restate) | +21.0 | +0.48% | 55.16 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +7.0 | +0.45% | 49.07 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1237 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7818 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：105 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 34.5k | +2023 | 100 | 94.37 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 20.3k | +154 | 100 | 82.59 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 48.6k | +184 | 40 | 75.24 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 35.7k | +102 | 100 | 74.42 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.6k | +52 | 100 | 62.19 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | +2023.0 | +6.22% | 91.52 |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | +154.0 | +0.77% | 70.70 |
| 3 | [Continue](https://github.com/continuedev/continue) | +102.0 | +0.29% | 64.41 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +184.0 | +0.38% | 62.58 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +52.0 | +2.00% | 58.47 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：92688 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77918 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：39490 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：27738 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：26477 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 64.4k | +497 | 100 | 87.99 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 30.4k | +161 | 100 | 83.19 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.5k | +126 | 100 | 82.10 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 11.1k | +162 | 100 | 74.91 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 27.8k | +493 | 100 | 72.54 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +497.0 | +0.78% | 77.64 |
| 2 | [agentmemory](https://github.com/rohitg00/agentmemory) | +493.0 | +1.80% | 71.42 |
| 3 | [Cognee](https://github.com/topoteretes/cognee) | +161.0 | +0.53% | 70.81 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +126.0 | +0.52% | 69.36 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +162.0 | +1.48% | 68.11 |

#### 新发现观察池

- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1187 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：945 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)：673 Stars；匹配度 3；The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：25314 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：21908 Stars；匹配度 2；Hindsight: Agent Memory That  Learns

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 89.7k | +598 | 100 | 81.50 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 39.3k | +164 | 100 | 76.08 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 51.9k | +101 | 100 | 74.95 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 35.8k | +106 | 100 | 74.54 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.4k | +72 | 100 | 72.88 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +598.0 | +0.67% | 74.90 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +164.0 | +0.42% | 67.15 |
| 3 | [GraphRAG](https://github.com/microsoft/graphrag) | +106.0 | +0.30% | 64.63 |
| 4 | [LlamaIndex](https://github.com/run-llama/llama_index) | +101.0 | +0.19% | 64.50 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +72.0 | +0.27% | 62.38 |

#### 新发现观察池

- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)：46648 Stars；匹配度 4；GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a git repository (Github, Gitlab, Azure, Local) or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration
- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38594 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：21003 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：135332 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77918 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 279.8k | +3062 | 100 | 91.11 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 172.7k | +1485 | 100 | 90.87 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 91.0k | +1684 | 100 | 84.22 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 24.9k | +255 | 85 | 82.42 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 242.1k | +8149 | 100 | 78.48 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Superpowers](https://github.com/obra/superpowers) | +3062.0 | +1.11% | 82.21 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | +1485.0 | +0.87% | 81.73 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | +1684.0 | +1.89% | 79.94 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +8149.0 | +3.48% | 79.47 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +255.0 | +1.04% | 71.71 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：54739 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [tt-a1i/archify](https://github.com/tt-a1i/archify)：35770 Stars；匹配度 3；Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.
- [googleworkspace/cli](https://github.com/googleworkspace/cli)：30660 Stars；匹配度 3；Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：135332 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：60639 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | 5.4k | +340 | 100 | 80.99 | 1000+ SaaS 的认证连接网关 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.2k | +67 | 100 | 80.03 | Python 官方 SDK |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.3k | +49 | 100 | 78.19 | TypeScript 官方 SDK |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.1k | +54 | 100 | 78.03 | MCP 规范与文档主仓库 |
| 5 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 90.0k | +174 | 100 | 77.46 | 生态入口不代表每个 Server 均成熟 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | +340.0 | +6.66% | 81.60 |
| 2 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +174.0 | +0.19% | 67.71 |
| 3 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +67.0 | +0.28% | 65.70 |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +54.0 | +0.60% | 64.42 |
| 5 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +49.0 | +0.37% | 63.81 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：93463 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：68132 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57491 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：41361 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：36642 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 15.6k | +137 | 100 | 81.93 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 25.6k | +93 | 100 | 81.15 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.8k | +21 | 85 | 63.74 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +137.0 | +0.88% | 70.12 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +93.0 | +0.37% | 67.57 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +21.0 | +0.76% | 53.07 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：554 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1454 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：663 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：507 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support
- [mahonzhan/awesome-agent-harness](https://github.com/mahonzhan/awesome-agent-harness)：270 Stars；匹配度 2；A curated awesome list of agent harnesses, agent frameworks, workflow frameworks, and emerging agent protocols.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 30.2k | +782 | 100 | 82.37 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.7k | +27 | 100 | 69.29 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.1k | +138 | 20 | 56.87 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +782.0 | +2.66% | 79.29 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +27.0 | +0.15% | 56.93 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +138.0 | +0.20% | 50.59 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21932 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：101913 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：69886 Stars；匹配度 1；🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：47555 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)：42634 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 14.8k | +231 | 100 | 84.04 | Agent 原生 Sandbox Runtime |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.4k | +93 | 100 | 79.97 | NVIDIA 自主 Agent 安全 Runtime |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | 13.6k | +75 | 100 | 79.63 | 企业 Agent 云端安全执行环境 |
| 4 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 11.4k | +106 | 100 | 73.20 | 国内高并发轻量 Sandbox 路线 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 3.7k | +94 | 100 | 72.57 | K8s 上 Agent 隔离工作负载 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +231.0 | +1.58% | 74.10 |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +93.0 | +1.11% | 68.10 |
| 3 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +94.0 | +2.61% | 66.69 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +75.0 | +0.55% | 66.32 |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +106.0 | +0.94% | 64.92 |

#### 新发现观察池

- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2067 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [Augani/dory](https://github.com/Augani/dory)：1546 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1127 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：941 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [yv1ing/Z3r0](https://github.com/yv1ing/Z3r0)：675 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 111.8k | +1502 | 100 | 91.36 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 22.0k | +216 | 100 | 83.94 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 24.1k | +75 | 100 | 80.38 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.6k | +35 | 100 | 68.86 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.3k | +10 | 65 | 57.45 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | +1502.0 | +1.36% | 82.72 |
| 2 | [CUA](https://github.com/trycua/cua) | +216.0 | +0.99% | 72.92 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +75.0 | +0.31% | 66.33 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +35.0 | +0.46% | 58.09 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +10.0 | +0.75% | 45.91 |

#### 新发现观察池

- [microsoft/Webwright](https://github.com/microsoft/Webwright)：5954 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4121 Stars；匹配度 2；Open-source, vision-first browser agent
- [oxylabs/browser-agent-py](https://github.com/oxylabs/browser-agent-py)：1549 Stars；匹配度 2；AI Browser Agent is an advanced Browser AI tool developed by Oxylabs AI Studio that automates real user browsing tasks using natural language instructions.
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1009 Stars；匹配度 2；Build browser agents for real world tasks
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：982 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 57.6k | +545 | 100 | 88.25 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 58.8k | +4916 | 100 | 83.20 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 12.9k | +46 | 40 | 61.44 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.0k | +9 | 100 | 57.18 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +4916.0 | +9.12% | 90.28 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +545.0 | +0.95% | 78.36 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +46.0 | +0.36% | 50.69 |
| 4 | [Plano](https://github.com/katanemo/plano) | +9.0 | +0.13% | 47.12 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：7675 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：5131 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5025 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44060 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：17061 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 34.0k | +370 | 100 | 86.35 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.3k | +101 | 100 | 80.50 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 21.7k | +143 | 100 | 74.90 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.7k | +16 | 100 | 65.04 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | +18 | 85 | 64.50 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +370.0 | +1.10% | 76.24 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +101.0 | +0.91% | 68.35 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +143.0 | +0.66% | 66.43 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +16.0 | +0.59% | 53.66 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +18.0 | +0.24% | 52.15 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1529 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：107 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：205 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：141 Stars；匹配度 2；无仓库描述
- [dreadnode/agent-lens](https://github.com/dreadnode/agent-lens)：114 Stars；匹配度 2；Agent observability and replay tooling for AI safety & interpretability research.

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 24.7k | +184 | 100 | 83.44 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 18.0k | +177 | 100 | 83.02 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.7k | +63 | 100 | 70.66 | 可复现评测任务框架 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.7k | +52 | 100 | 69.95 | 真实代码 Issue 基准 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.8k | +33 | 100 | 68.34 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [DeepEval](https://github.com/confident-ai/deepeval) | +177.0 | +0.99% | 71.75 |
| 2 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +184.0 | +0.75% | 71.74 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +63.0 | +2.42% | 64.01 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +52.0 | +0.91% | 60.71 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +33.0 | +0.57% | 57.79 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：371 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：489 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：365 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：327 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [h9-tec/llm-systems-engineering-roadmap](https://github.com/h9-tec/llm-systems-engineering-roadmap)：192 Stars；匹配度 3；A practical roadmap for mastering LLM internals, training, inference, RAG, agents, evaluation, and production architecture.

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 15.3k | +434 | 100 | 87.24 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.4k | +32 | 100 | 75.43 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.0k | +28 | 100 | 68.04 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 453 | +7 | 20 | 41.22 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +434.0 | +2.91% | 79.97 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +32.0 | +0.74% | 61.47 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +28.0 | +0.40% | 56.81 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +7.0 | +1.57% | 34.49 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：1980 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：553 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：307 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：199 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work
- [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)：3025 Stars；匹配度 2；Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.5k | +33 | 100 | 77.08 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 5.7k | +37 | 100 | 76.21 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.3k | +41 | 100 | 70.23 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | +37.0 | +0.66% | 62.25 |
| 2 | [Logto](https://github.com/logto-io/logto) | +33.0 | +0.23% | 61.65 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +41.0 | +0.29% | 59.07 |

#### 新发现观察池

- [Vorim-AI-Labs/vorim-mcp-server](https://github.com/Vorim-AI-Labs/vorim-mcp-server)：73 Stars；匹配度 3；MCP server for Vorim AI — AI agent identity, permissions, and audit trails. 19 tools for Claude, OpenAI, Cursor, VS Code, and any MCP-compatible client.
- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：58 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8502 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2700 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 37.1k | +137 | 100 | 82.92 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 11.9k | +146 | 100 | 74.49 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.4k | +35 | 65 | 64.16 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +137.0 | +0.37% | 69.85 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +146.0 | +1.24% | 67.17 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +35.0 | +0.31% | 52.89 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：794 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 120.2k | +4796 | 100 | 94.16 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | 202.7k | +1958 | 100 | 90.98 | 终端 Agent 架构参考 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 85.7k | +826 | 100 | 90.16 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 81.2k | +426 | 100 | 87.70 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 238.6k | +3567 | 100 | 84.02 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Codex](https://github.com/openai/codex) | +4796.0 | +4.16% | 88.31 |
| 2 | [herdr](https://github.com/herdrdev/herdr) | +1960.0 | +6.16% | 83.88 |
| 3 | [OpenCode](https://github.com/anomalyco/opencode) | +1958.0 | +0.98% | 81.95 |
| 4 | [OpenHands](https://github.com/OpenHands/OpenHands) | +826.0 | +0.97% | 80.85 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +3567.0 | +1.52% | 79.29 |

#### 新发现观察池

- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)：68533 Stars；匹配度 3；omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- [xai-org/grok-build](https://github.com/xai-org/grok-build)：26268 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [truefoundry/trueforge](https://github.com/truefoundry/trueforge)：4957 Stars；匹配度 3；The open-source agent harness - the runtime layer that turns an LLM into a working agent.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：244832 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：75705 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
