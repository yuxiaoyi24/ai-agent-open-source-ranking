# AI Agent 开源项目周榜（2026-08-10）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-08-05，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 39.3k | +403 | 100 | 88.18 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 28.5k | +123 | 100 | 83.35 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 12.7k | +99 | 100 | 81.81 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.1k | +45 | 100 | 79.63 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 56.9k | +239 | 100 | 78.95 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +564.2 | +1.45% | 79.20 |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | +334.6 | +0.59% | 71.41 |
| 3 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +172.2 | +0.61% | 71.24 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +138.6 | +1.10% | 70.43 |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | +180.6 | +0.67% | 67.81 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1919 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：850 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [swarmclawai/swarmclaw](https://github.com/swarmclawai/swarmclaw)：636 Stars；匹配度 3；Open-source self-hosted AI agent runtime and multi-agent framework for autonomous agent swarms. Agent memory, MCP tools, schedules, delegation, and 23+ LLM providers (Claude, GPT, Gemini, OpenRouter, Ollama). A practical Claude Code and LangChain alternative.
- [google/ax](https://github.com/google/ax)：1943 Stars；匹配度 2；An open source distributed agent runtime
- [GCWing/BitFun](https://github.com/GCWing/BitFun)：1639 Stars；匹配度 2；BitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 22.2k | +93 | 100 | 82.09 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.3k | +15 | 100 | 66.47 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.5k | +4 | 100 | 61.06 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +130.2 | +0.59% | 69.58 |
| 2 | [Restate](https://github.com/restatedev/restate) | +21.0 | +0.49% | 55.16 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +5.6 | +0.37% | 47.91 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1230 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7695 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 28.1k | +191 | 100 | 84.95 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 19.8k | +117 | 100 | 82.80 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 48.1k | +139 | 65 | 79.16 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 35.4k | +92 | 100 | 75.15 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.5k | +34 | 100 | 61.77 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | +267.4 | +0.96% | 74.15 |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | +163.8 | +0.83% | 71.12 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | +194.6 | +0.41% | 66.66 |
| 4 | [Continue](https://github.com/continuedev/continue) | +128.8 | +0.36% | 65.73 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +47.6 | +1.94% | 57.85 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：90253 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77379 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：37591 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：27257 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：26075 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 62.9k | +335 | 100 | 87.76 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 29.9k | +114 | 100 | 83.14 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.2k | +70 | 100 | 81.24 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 10.7k | +62 | 100 | 72.39 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 26.8k | +242 | 100 | 70.86 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +469.0 | +0.75% | 77.27 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +159.6 | +0.54% | 70.76 |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | +338.8 | +1.28% | 68.44 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +98.0 | +0.41% | 67.86 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +86.8 | +0.82% | 63.62 |

#### 新发现观察池

- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1149 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：853 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)：649 Stars；匹配度 3；The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：19430 Stars；匹配度 2；Hindsight: Agent Memory That  Learns
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：19019 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 87.2k | +277 | 100 | 79.97 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 38.7k | +174 | 100 | 77.41 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 51.5k | +130 | 100 | 76.79 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 35.4k | +107 | 100 | 75.64 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.2k | +51 | 100 | 72.84 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +387.8 | +0.45% | 72.24 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +243.6 | +0.63% | 69.56 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +182.0 | +0.35% | 67.78 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +149.8 | +0.42% | 66.61 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +71.4 | +0.27% | 62.33 |

#### 新发现观察池

- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)：45228 Stars；匹配度 4；GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a git repository (Github, Gitlab, Azure, Local) or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration
- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38531 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：19586 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：131825 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77379 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 269.9k | +3016 | 100 | 91.58 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 167.3k | +929 | 100 | 90.78 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 85.3k | +3617 | 100 | 88.42 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 24.1k | +206 | 100 | 85.14 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 211.7k | +7617 | 100 | 80.23 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [agent-skills](https://github.com/addyosmani/agent-skills) | +5063.8 | +6.20% | 88.50 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | +4222.4 | +1.58% | 83.16 |
| 3 | [mattpocock skills](https://github.com/mattpocock/skills) | +10663.8 | +5.23% | 82.95 |
| 4 | [Anthropic Skills](https://github.com/anthropics/skills) | +1300.6 | +0.78% | 81.56 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +288.4 | +1.21% | 74.90 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：46437 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [googleworkspace/cli](https://github.com/googleworkspace/cli)：30286 Stars；匹配度 3；Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：28518 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：131825 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：57789 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.0k | +63 | 100 | 80.89 | Python 官方 SDK |
| 2 | [Open Connector](https://github.com/oomol-lab/open-connector) | 4.5k | +207 | 100 | 80.28 | 1000+ SaaS 的认证连接网关 |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.1k | +36 | 100 | 78.26 | TypeScript 官方 SDK |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 8.9k | +41 | 100 | 78.22 | MCP 规范与文档主仓库 |
| 5 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 89.4k | +158 | 100 | 78.20 | 生态入口不代表每个 Server 均成熟 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | +289.8 | +6.75% | 80.79 |
| 2 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +221.2 | +0.25% | 69.03 |
| 3 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +88.2 | +0.37% | 67.25 |
| 4 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | +60.2 | +1.42% | 65.94 |
| 5 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +57.4 | +0.65% | 64.80 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：92030 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：65698 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57418 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：38335 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：35952 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [A2A](https://github.com/a2aproject/A2A) | 25.3k | +63 | 100 | 80.96 | Agent 到 Agent 的远程互操作 |
| 2 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 15.2k | +69 | 100 | 80.63 | Agent 到 UI 的事件协议 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.7k | +17 | 85 | 64.16 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +96.6 | +0.64% | 67.85 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +88.2 | +0.35% | 67.26 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +23.8 | +0.89% | 53.91 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：551 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1457 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：647 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：506 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support
- [mahonzhan/awesome-agent-harness](https://github.com/mahonzhan/awesome-agent-harness)：250 Stars；匹配度 2；A curated awesome list of agent harnesses, agent frameworks, workflow frameworks, and emerging agent protocols.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 28.8k | +164 | 100 | 76.89 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.6k | +22 | 100 | 69.67 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 69.8k | +86 | 20 | 56.44 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +229.6 | +0.80% | 69.34 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +30.8 | +0.18% | 57.62 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +120.4 | +0.17% | 49.85 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21890 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：96902 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：67527 Stars；匹配度 1；🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：46813 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)：41870 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 12.4k | +74 | 100 | 80.68 | Agent 原生 Sandbox Runtime |
| 2 | [E2B](https://github.com/e2b-dev/E2B) | 13.3k | +66 | 100 | 80.33 | 企业 Agent 云端安全执行环境 |
| 3 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.1k | +70 | 100 | 80.16 | NVIDIA 自主 Agent 安全 Runtime |
| 4 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 11.0k | +113 | 100 | 74.80 | 国内高并发轻量 Sandbox 路线 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 3.5k | +55 | 100 | 71.53 | K8s 上 Agent 隔离工作负载 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +98.0 | +1.23% | 68.55 |
| 2 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +103.6 | +0.84% | 68.43 |
| 3 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +158.2 | +1.45% | 67.92 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +92.4 | +0.70% | 67.63 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +77.0 | +2.26% | 64.93 |

#### 新发现观察池

- [pullrun/pullrun](https://github.com/pullrun/pullrun)：121 Stars；匹配度 3；The AI agent sandbox runtime. Boot any OCI image as a Firecracker microVM, Linux container, or Apple Silicon VM in ~400 ms — zero-copy DAG storage, P2P image sync, native MCP for opencode/Claude Code/Cursor.
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：1911 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1073 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [yv1ing/Z3r0](https://github.com/yv1ing/Z3r0)：612 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：578 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 108.5k | +611 | 100 | 90.34 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 21.1k | +139 | 100 | 83.50 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 23.8k | +57 | 100 | 80.56 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.5k | +34 | 100 | 69.88 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.3k | +7 | 85 | 60.36 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | +855.4 | +0.79% | 80.80 |
| 2 | [CUA](https://github.com/trycua/cua) | +194.6 | +0.93% | 72.24 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +79.8 | +0.34% | 66.68 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +47.6 | +0.64% | 59.96 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +9.8 | +0.75% | 48.80 |

#### 新发现观察池

- [microsoft/Webwright](https://github.com/microsoft/Webwright)：5901 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4111 Stars；匹配度 2；Open-source, vision-first browser agent
- [oxylabs/browser-agent-py](https://github.com/oxylabs/browser-agent-py)：1442 Stars；匹配度 2；AI Browser Agent is an advanced Browser AI tool developed by Oxylabs AI Studio that automates real user browsing tasks using natural language instructions.
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1010 Stars；匹配度 2；Build browser agents for real world tasks
- [LvcidPsyche/auto-browser](https://github.com/LvcidPsyche/auto-browser)：758 Stars；匹配度 2；Give your AI agent a real browser — with a human in the loop. Open-source MCP-native browser agent.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 56.0k | +393 | 100 | 88.26 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 44.5k | +4402 | 100 | 83.60 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 12.7k | +30 | 65 | 64.88 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.0k | +28 | 100 | 61.64 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +6162.8 | +15.35% | 91.80 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +550.2 | +0.99% | 78.46 |
| 3 | [Plano](https://github.com/katanemo/plano) | +39.2 | +0.56% | 55.03 |
| 4 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +42.0 | +0.33% | 53.93 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：7182 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：4931 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：2725 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：43953 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：16972 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 32.8k | +238 | 100 | 85.91 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.0k | +62 | 100 | 79.91 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 21.3k | +143 | 100 | 76.12 | 观测评测一体化 |
| 4 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | +11 | 100 | 66.28 | LLM/Agent OTel instrumentation |
| 5 | [OpenLIT](https://github.com/openlit/openlit) | 2.7k | +8 | 100 | 63.87 | AI Engineering 多治理能力 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +333.2 | +1.02% | 75.53 |
| 2 | [Opik](https://github.com/comet-ml/opik) | +200.2 | +0.95% | 68.68 |
| 3 | [Phoenix](https://github.com/Arize-ai/phoenix) | +86.8 | +0.80% | 67.35 |
| 4 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +15.4 | +0.21% | 53.58 |
| 5 | [OpenLIT](https://github.com/openlit/openlit) | +11.2 | +0.42% | 51.62 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1508 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：135 Stars；匹配度 2；无仓库描述
- [dreadnode/agent-lens](https://github.com/dreadnode/agent-lens)：111 Stars；匹配度 2；Agent observability and replay tooling for AI safety & interpretability research.

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 24.1k | +154 | 100 | 84.00 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 17.5k | +79 | 100 | 81.26 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.5k | +37 | 100 | 69.68 | 可复现评测任务框架 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.6k | +33 | 100 | 69.48 | 真实代码 Issue 基准 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.7k | +5 | 100 | 63.68 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +215.6 | +0.90% | 72.81 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +110.6 | +0.64% | 68.65 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +51.8 | +2.09% | 62.33 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +46.2 | +0.83% | 59.94 |
| 5 | [OpenEvals](https://github.com/langchain-ai/openevals) | +11.2 | +0.97% | 52.00 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：370 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：545 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：327 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [h9-tec/llm-systems-engineering-roadmap](https://github.com/h9-tec/llm-systems-engineering-roadmap)：179 Stars；匹配度 3；A practical roadmap for mastering LLM internals, training, inference, RAG, agents, evaluation, and production architecture.
- [Infinity-AILab/DeepResearchEval](https://github.com/Infinity-AILab/DeepResearchEval)：142 Stars；匹配度 3；DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation.

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 14.4k | +239 | 100 | 85.83 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.3k | +28 | 100 | 76.14 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 6.9k | +24 | 100 | 68.60 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 441 | +3 | 20 | 39.31 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +334.6 | +2.36% | 77.50 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +39.2 | +0.92% | 62.82 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +33.6 | +0.49% | 57.86 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +4.2 | +0.96% | 31.06 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：1959 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：520 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：275 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：195 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work
- [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)：2980 Stars；匹配度 2；Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.3k | +32 | 100 | 78.01 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 5.6k | +26 | 100 | 76.13 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.2k | +27 | 100 | 69.96 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Logto](https://github.com/logto-io/logto) | +44.8 | +0.31% | 63.32 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | +36.4 | +0.66% | 62.15 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +37.8 | +0.27% | 58.62 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：53 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8549 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2714 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity)：1187 Stars；匹配度 2；多线程全自动注册free 绕过接码使用codex
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：755 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 36.7k | +186 | 100 | 85.09 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 11.5k | +100 | 100 | 74.30 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.2k | +28 | 65 | 64.50 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +260.4 | +0.71% | 73.76 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +140.0 | +1.23% | 66.90 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +39.2 | +0.35% | 53.52 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：794 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：152 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | 195.6k | +1984 | 100 | 91.43 | 终端 Agent 架构参考 |
| 2 | [Codex](https://github.com/openai/codex) | 105.0k | +975 | 100 | 91.31 | 完整 Coding Agent Harness 源码样本 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 83.6k | +422 | 100 | 88.88 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 79.6k | +299 | 100 | 87.62 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 228.1k | +2320 | 100 | 83.94 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [herdr](https://github.com/herdrdev/herdr) | +2973.6 | +12.13% | 91.35 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | +2777.6 | +1.43% | 82.87 |
| 3 | [Codex](https://github.com/openai/codex) | +1365.0 | +1.31% | 82.62 |
| 4 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +3248.0 | +1.44% | 79.13 |
| 5 | [OpenHands](https://github.com/OpenHands/OpenHands) | +590.8 | +0.71% | 78.61 |

#### 新发现观察池

- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)：67592 Stars；匹配度 3；omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- [xai-org/grok-build](https://github.com/xai-org/grok-build)：24556 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：239076 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：73704 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：46436 Stars；匹配度 2；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
