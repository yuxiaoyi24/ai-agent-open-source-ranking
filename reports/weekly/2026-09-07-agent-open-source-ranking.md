# AI Agent 开源项目周榜（2026-09-07）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-08-31，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 41.1k | +405 | 100 | 86.84 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 29.2k | +143 | 100 | 82.74 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 13.4k | +125 | 100 | 81.45 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.4k | +94 | 100 | 80.95 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 58.2k | +329 | 100 | 78.92 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +405.0 | +0.99% | 76.65 |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | +329.0 | +0.57% | 71.30 |
| 3 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +143.0 | +0.49% | 70.10 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +125.0 | +0.94% | 69.65 |
| 5 | [Google ADK Python](https://github.com/google/adk-python) | +94.0 | +0.44% | 67.62 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1899 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：863 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3809 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.
- [GCWing/BitFun](https://github.com/GCWing/BitFun)：2084 Stars；匹配度 2；OpenBitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.
- [google/ax](https://github.com/google/ax)：1989 Stars；匹配度 2；An open source distributed agent runtime

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 22.9k | +251 | 100 | 84.56 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.4k | +32 | 100 | 67.93 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +7 | 100 | 61.75 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +251.0 | +1.11% | 73.95 |
| 2 | [Restate](https://github.com/restatedev/restate) | +32.0 | +0.73% | 57.72 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +7.0 | +0.45% | 49.07 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1239 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7887 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：108 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 35.8k | +1281 | 100 | 91.93 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 20.5k | +237 | 100 | 84.26 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 48.8k | +182 | 40 | 75.21 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 35.8k | +107 | 100 | 74.57 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.7k | +37 | 100 | 60.65 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | +1281.0 | +3.71% | 86.52 |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | +237.0 | +1.17% | 73.69 |
| 3 | [Continue](https://github.com/continuedev/continue) | +107.0 | +0.30% | 64.68 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +182.0 | +0.37% | 62.52 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +37.0 | +1.40% | 55.59 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：93363 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78070 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：39627 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：27858 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：26678 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 64.8k | +411 | 100 | 87.32 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 30.5k | +181 | 100 | 83.60 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.6k | +137 | 85 | 80.14 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 11.2k | +106 | 100 | 73.18 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 28.1k | +290 | 100 | 70.26 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +411.0 | +0.64% | 76.41 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +181.0 | +0.60% | 71.53 |
| 3 | [Letta](https://github.com/letta-ai/letta) | +137.0 | +0.56% | 67.62 |
| 4 | [agentmemory](https://github.com/rohitg00/agentmemory) | +290.0 | +1.04% | 67.23 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +106.0 | +0.95% | 64.93 |

#### 新发现观察池

- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1202 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1037 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)：680 Stars；匹配度 3；The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：26035 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：22840 Stars；匹配度 2；Hindsight: Agent Memory That Learns

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 90.2k | +466 | 100 | 80.64 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 39.4k | +163 | 100 | 76.06 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.0k | +118 | 100 | 75.43 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 35.9k | +113 | 100 | 74.75 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.4k | +69 | 100 | 72.75 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +466.0 | +0.52% | 73.34 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +163.0 | +0.41% | 67.11 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +118.0 | +0.23% | 65.35 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +113.0 | +0.32% | 64.99 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +69.0 | +0.26% | 62.14 |

#### 新发现观察池

- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)：47091 Stars；匹配度 4；GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a git repository (Github, Gitlab, Azure, Local) or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration
- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38617 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：21607 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：136444 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78070 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Anthropic Skills](https://github.com/anthropics/skills) | 174.9k | +2213 | 100 | 91.28 | 官方 Skill 样本库 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | 282.5k | +2734 | 100 | 90.98 | Skill 驱动的软件工程方法 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 92.6k | +1642 | 100 | 84.17 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 25.1k | +211 | 85 | 81.71 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 255.0k | +12909 | 100 | 80.33 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [mattpocock skills](https://github.com/mattpocock/skills) | +12909.0 | +5.33% | 83.16 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | +2213.0 | +1.28% | 82.56 |
| 3 | [Superpowers](https://github.com/obra/superpowers) | +2734.0 | +0.98% | 81.95 |
| 4 | [agent-skills](https://github.com/addyosmani/agent-skills) | +1642.0 | +1.80% | 79.79 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +211.0 | +0.85% | 70.39 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：56442 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [tt-a1i/archify](https://github.com/tt-a1i/archify)：51241 Stars；匹配度 3；Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.
- [googleworkspace/cli](https://github.com/googleworkspace/cli)：30765 Stars；匹配度 3；Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：136444 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：61469 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.2k | +53 | 100 | 79.31 | Python 官方 SDK |
| 2 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.1k | +62 | 100 | 78.52 | MCP 规范与文档主仓库 |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.3k | +54 | 100 | 78.51 | TypeScript 官方 SDK |
| 4 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 90.1k | +136 | 100 | 76.72 | 生态入口不代表每个 Server 均成熟 |
| 5 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.4k | +36 | 100 | 75.86 | 企业工具网关和统一治理 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | +133.0 | +2.44% | 68.45 |
| 2 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +136.0 | +0.15% | 66.39 |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +62.0 | +0.68% | 65.28 |
| 4 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +53.0 | +0.22% | 64.42 |
| 5 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +54.0 | +0.41% | 64.37 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：94508 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：69170 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57494 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：42474 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：36862 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [A2A](https://github.com/a2aproject/A2A) | 25.7k | +106 | 100 | 81.58 | Agent 到 Agent 的远程互操作 |
| 2 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 15.8k | +112 | 100 | 81.19 | Agent 到 UI 的事件协议 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.8k | +23 | 85 | 64.07 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +112.0 | +0.72% | 68.78 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +106.0 | +0.41% | 68.32 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +23.0 | +0.83% | 53.65 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：554 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1454 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：668 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：507 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support
- [mahonzhan/awesome-agent-harness](https://github.com/mahonzhan/awesome-agent-harness)：277 Stars；匹配度 2；A curated awesome list of agent harnesses, agent frameworks, workflow frameworks, and emerging agent protocols.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 30.9k | +757 | 100 | 82.17 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.7k | +25 | 100 | 69.06 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.2k | +136 | 20 | 56.83 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +757.0 | +2.51% | 78.85 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +25.0 | +0.14% | 56.54 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +136.0 | +0.19% | 50.51 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21944 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：102767 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：71084 Stars；匹配度 1；🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：47812 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)：42877 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 15.0k | +161 | 100 | 82.52 | Agent 原生 Sandbox Runtime |
| 2 | [E2B](https://github.com/e2b-dev/E2B) | 13.7k | +89 | 100 | 80.23 | 企业 Agent 云端安全执行环境 |
| 3 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 11.8k | +410 | 100 | 79.81 | 国内高并发轻量 Sandbox 路线 |
| 4 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.5k | +88 | 100 | 79.76 | NVIDIA 自主 Agent 安全 Runtime |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 3.8k | +69 | 100 | 70.97 | K8s 上 Agent 隔离工作负载 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +410.0 | +3.59% | 77.07 |
| 2 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +161.0 | +1.08% | 71.30 |
| 3 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +88.0 | +1.04% | 67.69 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +89.0 | +0.65% | 67.38 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +69.0 | +1.87% | 63.67 |

#### 新发现观察池

- [pullrun/pullrun](https://github.com/pullrun/pullrun)：129 Stars；匹配度 3；The AI agent sandbox runtime. Boot any OCI image as a Firecracker microVM, Linux container, or Apple Silicon VM in ~400 ms — zero-copy DAG storage, P2P image sync, native MCP for opencode/Claude Code/Cursor.
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2110 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [Augani/dory](https://github.com/Augani/dory)：1569 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1132 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1019 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 112.8k | +1023 | 100 | 90.92 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 22.3k | +234 | 100 | 84.26 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 24.2k | +60 | 100 | 79.68 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.6k | +31 | 100 | 68.47 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.3k | +9 | 65 | 57.11 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | +1023.0 | +0.92% | 81.83 |
| 2 | [CUA](https://github.com/trycua/cua) | +234.0 | +1.06% | 73.48 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +60.0 | +0.25% | 65.09 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +31.0 | +0.41% | 57.39 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +9.0 | +0.67% | 45.27 |

#### 新发现观察池

- [feder-cr/AIHawk](https://github.com/feder-cr/AIHawk)：30321 Stars；匹配度 3；Open-source AI browser agent for web automation: a web browsing agent and computer-use agent in plain English. Browser MCP for Claude Code and Gemini CLI.
- [microsoft/Webwright](https://github.com/microsoft/Webwright)：5960 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4125 Stars；匹配度 2；Open-source, vision-first browser agent
- [oxylabs/browser-agent-py](https://github.com/oxylabs/browser-agent-py)：1565 Stars；匹配度 2；AI Browser Agent is an advanced Browser AI tool developed by Oxylabs AI Studio that automates real user browsing tasks using natural language instructions.
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1008 Stars；匹配度 2；Build browser agents for real world tasks

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 58.2k | +545 | 100 | 88.25 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 62.1k | +3310 | 100 | 79.80 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 12.9k | +61 | 40 | 62.37 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.0k | +14 | 85 | 56.18 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3310.0 | +5.63% | 83.34 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +545.0 | +0.95% | 78.35 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +61.0 | +0.47% | 52.33 |
| 4 | [Plano](https://github.com/katanemo/plano) | +14.0 | +0.20% | 47.06 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：7846 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：5176 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5072 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44092 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：17090 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 34.3k | +313 | 100 | 85.71 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.3k | +96 | 100 | 80.32 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 21.8k | +140 | 100 | 74.83 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.7k | +12 | 100 | 64.12 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | +5 | 85 | 60.99 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +313.0 | +0.92% | 75.04 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +96.0 | +0.85% | 68.00 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +140.0 | +0.65% | 66.29 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +12.0 | +0.44% | 52.00 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +5.0 | +0.07% | 45.95 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1531 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：109 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：205 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：143 Stars；匹配度 2；无仓库描述
- [dreadnode/agent-lens](https://github.com/dreadnode/agent-lens)：115 Stars；匹配度 2；Agent observability and replay tooling for AI safety & interpretability research.

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 24.9k | +189 | 100 | 83.54 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 18.1k | +148 | 100 | 82.34 | LLM/Agent Evaluation Framework |
| 3 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.8k | +41 | 100 | 69.09 | 真实代码 Issue 基准 |
| 4 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.7k | +44 | 100 | 68.90 | 可复现评测任务框架 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.8k | +7 | 100 | 63.70 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +189.0 | +0.77% | 71.91 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +148.0 | +0.82% | 70.52 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +44.0 | +1.65% | 60.70 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +41.0 | +0.71% | 59.14 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +7.0 | +0.12% | 49.56 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：372 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：489 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：407 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：328 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [h9-tec/llm-systems-engineering-roadmap](https://github.com/h9-tec/llm-systems-engineering-roadmap)：194 Stars；匹配度 3；A practical roadmap for mastering LLM internals, training, inference, RAG, agents, evaluation, and production architecture.

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 16.4k | +1084 | 100 | 93.92 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.4k | +33 | 100 | 75.54 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.1k | +42 | 100 | 69.39 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 453 | +0 | 20 | 33.63 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +1084.0 | +7.06% | 92.56 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +33.0 | +0.75% | 61.66 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +42.0 | +0.60% | 59.20 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：1986 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：559 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：313 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：201 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work
- [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)：3042 Stars；匹配度 2；Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.5k | +30 | 100 | 76.80 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 5.7k | +41 | 100 | 76.57 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.4k | +57 | 100 | 71.28 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | +41.0 | +0.72% | 62.90 |
| 2 | [Logto](https://github.com/logto-io/logto) | +30.0 | +0.21% | 61.14 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +57.0 | +0.40% | 60.93 |

#### 新发现观察池

- [Vorim-AI-Labs/vorim-mcp-server](https://github.com/Vorim-AI-Labs/vorim-mcp-server)：73 Stars；匹配度 3；MCP server for Vorim AI — AI agent identity, permissions, and audit trails. 19 tools for Claude, OpenAI, Cursor, VS Code, and any MCP-compatible client.
- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：59 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8503 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2699 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 37.2k | +92 | 100 | 81.65 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12.0k | +96 | 100 | 72.87 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.5k | +114 | 65 | 68.23 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +92.0 | +0.25% | 67.60 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +96.0 | +0.80% | 64.20 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +114.0 | +1.00% | 60.17 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：794 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 122.0k | +1829 | 100 | 91.52 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | 205.4k | +2728 | 100 | 91.35 | 终端 Agent 架构参考 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 86.4k | +686 | 100 | 89.46 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 81.6k | +496 | 100 | 88.23 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 242.7k | +4052 | 100 | 84.20 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [herdr](https://github.com/herdrdev/herdr) | +2106.0 | +6.24% | 84.08 |
| 2 | [Codex](https://github.com/openai/codex) | +1829.0 | +1.52% | 83.04 |
| 3 | [OpenCode](https://github.com/anomalyco/opencode) | +2728.0 | +1.35% | 82.69 |
| 4 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +4052.0 | +1.70% | 79.65 |
| 5 | [OpenHands](https://github.com/OpenHands/OpenHands) | +686.0 | +0.80% | 79.57 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：26524 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [truefoundry/trueforge](https://github.com/truefoundry/trueforge)：5274 Stars；匹配度 3；The open-source agent harness - the runtime layer that turns an LLM into a working agent.
- [Waishnav/devspace](https://github.com/Waishnav/devspace)：4503 Stars；匹配度 3；Minimal Coding Agent Harness on MCP for ChatGPT, Claude, Hermes, Grok Bot, OpenClaw
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：251721 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：76196 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
