# AI Agent 开源项目周榜（2026-08-24）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-08-17，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 40.3k | +482 | 100 | 87.52 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 28.9k | +208 | 100 | 84.04 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 13.1k | +227 | 100 | 83.95 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.2k | +90 | 100 | 80.79 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 57.5k | +346 | 100 | 79.08 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +482.0 | +1.21% | 77.94 |
| 2 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +227.0 | +1.77% | 74.28 |
| 3 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +208.0 | +0.72% | 72.44 |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | +346.0 | +0.61% | 71.62 |
| 5 | [Google ADK Python](https://github.com/google/adk-python) | +90.0 | +0.43% | 67.36 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1895 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：857 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3795 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.
- [google/ax](https://github.com/google/ax)：1967 Stars；匹配度 2；An open source distributed agent runtime
- [GCWing/BitFun](https://github.com/GCWing/BitFun)：1809 Stars；匹配度 2；BitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 22.5k | +135 | 100 | 82.24 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.3k | +31 | 100 | 67.80 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.5k | +17 | 100 | 64.74 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +135.0 | +0.60% | 69.80 |
| 2 | [Restate](https://github.com/restatedev/restate) | +31.0 | +0.72% | 57.53 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +17.0 | +1.11% | 54.50 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1234 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7782 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 32.5k | +3833 | 100 | 98.05 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 20.1k | +205 | 100 | 83.67 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 48.4k | +160 | 40 | 74.78 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 35.6k | +102 | 100 | 74.41 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.6k | +58 | 100 | 62.75 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | +3833.0 | +13.36% | 99.02 |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | +205.0 | +1.03% | 72.66 |
| 3 | [Continue](https://github.com/continuedev/continue) | +102.0 | +0.29% | 64.41 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +160.0 | +0.33% | 61.78 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +58.0 | +2.29% | 59.56 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：91618 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77730 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：38785 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：27587 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：26316 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 63.9k | +507 | 100 | 88.06 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 30.2k | +130 | 100 | 82.47 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.4k | +101 | 100 | 81.35 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 10.9k | +206 | 100 | 76.02 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 27.3k | +239 | 100 | 69.50 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +507.0 | +0.80% | 77.78 |
| 2 | [MemOS](https://github.com/MemTensor/MemOS) | +206.0 | +1.92% | 70.19 |
| 3 | [Cognee](https://github.com/topoteretes/cognee) | +130.0 | +0.43% | 69.53 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +101.0 | +0.42% | 68.04 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | +239.0 | +0.88% | 65.91 |

#### 新发现观察池

- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1176 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：927 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)：666 Stars；匹配度 3；The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：24046 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：20983 Stars；匹配度 2；Hindsight: Agent Memory That  Learns

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 89.1k | +480 | 100 | 80.72 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 39.1k | +209 | 100 | 76.89 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 51.8k | +141 | 100 | 75.98 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 35.6k | +118 | 100 | 74.88 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.3k | +67 | 100 | 72.65 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +480.0 | +0.54% | 73.52 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +209.0 | +0.54% | 68.60 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +141.0 | +0.27% | 66.33 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +118.0 | +0.33% | 65.23 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +67.0 | +0.26% | 61.98 |

#### 新发现观察池

- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)：45701 Stars；匹配度 4；GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a git repository (Github, Gitlab, Azure, Local) or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration
- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38570 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：20446 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：133735 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77730 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 276.7k | +3868 | 100 | 91.42 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 171.2k | +1429 | 100 | 90.84 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 89.3k | +1523 | 100 | 84.04 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 24.6k | +284 | 85 | 82.85 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 234.0k | +14601 | 100 | 81.66 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [mattpocock skills](https://github.com/mattpocock/skills) | +14601.0 | +6.66% | 85.81 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | +3868.0 | +1.42% | 82.84 |
| 3 | [Anthropic Skills](https://github.com/anthropics/skills) | +1429.0 | +0.84% | 81.68 |
| 4 | [agent-skills](https://github.com/addyosmani/agent-skills) | +1523.0 | +1.74% | 79.62 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +284.0 | +1.17% | 72.51 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：49817 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [googleworkspace/cli](https://github.com/googleworkspace/cli)：30524 Stars；匹配度 3；Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：29534 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：133735 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：59103 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | 5.1k | +368 | 100 | 82.22 | 1000+ SaaS 的认证连接网关 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.1k | +73 | 100 | 80.29 | Python 官方 SDK |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.0k | +62 | 100 | 78.51 | MCP 规范与文档主仓库 |
| 4 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.2k | +53 | 100 | 78.44 | TypeScript 官方 SDK |
| 5 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 89.8k | +197 | 100 | 77.84 | 生态入口不代表每个 Server 均成熟 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | +368.0 | +7.77% | 84.16 |
| 2 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +197.0 | +0.22% | 68.39 |
| 3 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +73.0 | +0.30% | 66.18 |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +62.0 | +0.69% | 65.29 |
| 5 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +53.0 | +0.40% | 64.26 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：92723 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：67298 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57458 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：40183 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：36403 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 15.5k | +168 | 100 | 82.71 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 25.5k | +99 | 100 | 81.35 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.8k | +28 | 100 | 67.04 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +168.0 | +1.10% | 71.56 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +99.0 | +0.39% | 67.93 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +28.0 | +1.03% | 57.25 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：554 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1455 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：658 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：507 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support
- [mahonzhan/awesome-agent-harness](https://github.com/mahonzhan/awesome-agent-harness)：264 Stars；匹配度 2；A curated awesome list of agent harnesses, agent frameworks, workflow frameworks, and emerging agent protocols.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 29.4k | +407 | 100 | 79.18 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.6k | +34 | 100 | 69.97 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.0k | +115 | 20 | 56.31 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +407.0 | +1.40% | 73.45 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +34.0 | +0.19% | 58.14 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +115.0 | +0.16% | 49.60 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21917 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：99512 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：69101 Stars；匹配度 1；🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：47313 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)：42376 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 14.6k | +650 | 100 | 90.07 | Agent 原生 Sandbox Runtime |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.3k | +134 | 100 | 81.52 | NVIDIA 自主 Agent 安全 Runtime |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | 13.5k | +101 | 100 | 80.67 | 企业 Agent 云端安全执行环境 |
| 4 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 11.3k | +155 | 100 | 74.72 | 国内高并发轻量 Sandbox 路线 |
| 5 | [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) | 5.0k | +65 | 100 | 70.75 | 无完整容器的 OS 级限制 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +650.0 | +4.65% | 85.46 |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +134.0 | +1.63% | 70.96 |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | +101.0 | +0.75% | 68.20 |
| 4 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +155.0 | +1.39% | 67.72 |
| 5 | [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) | +65.0 | +1.30% | 62.49 |

#### 新发现观察池

- [pullrun/pullrun](https://github.com/pullrun/pullrun)：128 Stars；匹配度 3；The AI agent sandbox runtime. Boot any OCI image as a Firecracker microVM, Linux container, or Apple Silicon VM in ~400 ms — zero-copy DAG storage, P2P image sync, native MCP for opencode/Claude Code/Cursor.
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2022 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1114 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：833 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [yv1ing/Z3r0](https://github.com/yv1ing/Z3r0)：630 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 110.3k | +827 | 100 | 90.21 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 21.8k | +400 | 100 | 86.58 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 24.0k | +71 | 100 | 80.20 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.5k | +36 | 100 | 68.94 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.3k | +8 | 65 | 56.71 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | +827.0 | +0.76% | 80.55 |
| 2 | [CUA](https://github.com/trycua/cua) | +400.0 | +1.87% | 77.78 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +71.0 | +0.30% | 66.02 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +36.0 | +0.48% | 58.26 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +8.0 | +0.61% | 44.59 |

#### 新发现观察池

- [microsoft/Webwright](https://github.com/microsoft/Webwright)：5939 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4121 Stars；匹配度 2；Open-source, vision-first browser agent
- [oxylabs/browser-agent-py](https://github.com/oxylabs/browser-agent-py)：1490 Stars；匹配度 2；AI Browser Agent is an advanced Browser AI tool developed by Oxylabs AI Studio that automates real user browsing tasks using natural language instructions.
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1009 Stars；匹配度 2；Build browser agents for real world tasks
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：895 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 57.1k | +605 | 100 | 88.65 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 53.9k | +4694 | 100 | 83.47 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 12.8k | +70 | 40 | 62.82 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.0k | +17 | 100 | 59.00 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +4694.0 | +9.54% | 91.04 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +605.0 | +1.07% | 79.12 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +70.0 | +0.55% | 53.16 |
| 4 | [Plano](https://github.com/katanemo/plano) | +17.0 | +0.24% | 50.32 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：7521 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：5056 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：4211 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44027 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：17022 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 33.6k | +385 | 100 | 86.51 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.2k | +78 | 100 | 79.54 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 21.6k | +140 | 100 | 74.82 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.7k | +24 | 100 | 66.45 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | +12 | 100 | 65.56 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +385.0 | +1.16% | 76.55 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +78.0 | +0.70% | 66.64 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +140.0 | +0.65% | 66.30 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +24.0 | +0.89% | 56.21 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +12.0 | +0.16% | 52.31 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1522 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：102 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：217 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：139 Stars；匹配度 2；无仓库描述
- [dreadnode/agent-lens](https://github.com/dreadnode/agent-lens)：113 Stars；匹配度 2；Agent observability and replay tooling for AI safety & interpretability research.

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 24.5k | +215 | 100 | 84.01 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 17.8k | +185 | 100 | 83.18 | LLM/Agent Evaluation Framework |
| 3 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.7k | +44 | 100 | 69.32 | 真实代码 Issue 基准 |
| 4 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.6k | +45 | 100 | 69.01 | 可复现评测任务框架 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.8k | +10 | 100 | 64.66 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +215.0 | +0.89% | 72.78 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +185.0 | +1.05% | 72.08 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +45.0 | +1.76% | 60.99 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +44.0 | +0.78% | 59.61 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +10.0 | +0.17% | 51.27 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：371 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：490 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：327 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：266 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [h9-tec/llm-systems-engineering-roadmap](https://github.com/h9-tec/llm-systems-engineering-roadmap)：187 Stars；匹配度 3；A practical roadmap for mastering LLM internals, training, inference, RAG, agents, evaluation, and production architecture.

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 14.9k | +234 | 100 | 84.10 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.3k | +37 | 100 | 75.94 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.0k | +40 | 100 | 69.21 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 446 | +1 | 20 | 35.83 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +234.0 | +1.59% | 74.20 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +37.0 | +0.86% | 62.42 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +40.0 | +0.57% | 58.91 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +1.0 | +0.22% | 24.76 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：1972 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：547 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：298 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：197 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work
- [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)：3009 Stars；匹配度 2；Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.4k | +90 | 100 | 80.33 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 5.6k | +35 | 100 | 76.01 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.3k | +52 | 100 | 70.98 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Logto](https://github.com/logto-io/logto) | +90.0 | +0.63% | 67.43 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | +35.0 | +0.62% | 61.91 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +52.0 | +0.37% | 60.41 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：56 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8507 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2699 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity)：1209 Stars；匹配度 2；多线程全自动注册free 绕过接码使用codex
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：755 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 37.0k | +199 | 100 | 84.15 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 11.8k | +103 | 100 | 73.11 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.3k | +30 | 65 | 63.67 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +199.0 | +0.54% | 72.06 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +103.0 | +0.88% | 64.69 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +30.0 | +0.27% | 52.04 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：794 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：152 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 115.4k | +9122 | 100 | 98.58 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | 200.7k | +2546 | 100 | 91.28 | 终端 Agent 架构参考 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 84.9k | +643 | 100 | 89.20 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 80.7k | +618 | 100 | 89.01 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 235.0k | +3490 | 100 | 84.01 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Codex](https://github.com/openai/codex) | +9122.0 | +8.58% | 97.16 |
| 2 | [herdr](https://github.com/herdrdev/herdr) | +2035.0 | +6.83% | 85.17 |
| 3 | [OpenCode](https://github.com/anomalyco/opencode) | +2546.0 | +1.28% | 82.57 |
| 4 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +3490.0 | +1.51% | 79.26 |
| 5 | [OpenHands](https://github.com/OpenHands/OpenHands) | +643.0 | +0.76% | 79.15 |

#### 新发现观察池

- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)：68300 Stars；匹配度 3；omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- [xai-org/grok-build](https://github.com/xai-org/grok-build)：25949 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：242584 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：75033 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：46641 Stars；匹配度 2；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
