# AI Agent 开源项目周榜（2026-09-21）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-09-14，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 42.0k | +449 | 100 | 87.26 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 29.6k | +179 | 100 | 83.53 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 13.6k | +131 | 100 | 81.65 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.6k | +55 | 100 | 79.25 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 58.8k | +347 | 100 | 79.12 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +449.0 | +1.08% | 77.36 |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | +347.0 | +0.59% | 71.63 |
| 3 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +179.0 | +0.61% | 71.47 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +131.0 | +0.97% | 69.95 |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | +205.0 | +0.73% | 68.61 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1896 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：870 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：6947 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3815 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.
- [GCWing/OpenBitFun](https://github.com/GCWing/OpenBitFun)：2304 Stars；匹配度 2；OpenBitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 23.2k | +196 | 100 | 83.61 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.5k | +40 | 100 | 68.75 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +8 | 100 | 62.17 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +196.0 | +0.85% | 72.20 |
| 2 | [Restate](https://github.com/restatedev/restate) | +40.0 | +0.91% | 59.18 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +8.0 | +0.51% | 49.80 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1246 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7976 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：122 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | 23.8k | +1101 | 100 | 92.36 | 独立 Context Manager 的直接样本 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | 38.2k | +1170 | 100 | 91.49 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 49.1k | +143 | 40 | 74.45 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 36.0k | +67 | 100 | 73.13 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.7k | +24 | 100 | 58.95 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | +1101.0 | +4.85% | 88.46 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | +1170.0 | +3.16% | 85.48 |
| 3 | [Continue](https://github.com/continuedev/continue) | +67.0 | +0.19% | 62.11 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +143.0 | +0.29% | 61.15 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +24.0 | +0.89% | 52.45 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：94360 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78511 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：39876 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：28075 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：27031 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 65.7k | +477 | 100 | 87.86 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 30.9k | +198 | 100 | 83.93 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.8k | +85 | 100 | 80.82 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 11.5k | +186 | 100 | 75.53 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 28.7k | +242 | 100 | 69.58 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +477.0 | +0.73% | 77.36 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +198.0 | +0.65% | 72.09 |
| 3 | [MemOS](https://github.com/MemTensor/MemOS) | +186.0 | +1.64% | 69.17 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +85.0 | +0.34% | 67.05 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | +242.0 | +0.85% | 65.95 |

#### 新发现观察池

- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1232 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1069 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：961 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)：707 Stars；匹配度 3；Git-native persistent memory for AI coding agents. Implements Google OKF v0.2 with sub-300µs in-memory BM25 search, embedded MCP server, and progressive disclosure. Slashes token bloat by 80% with zero external databases or dependencies. Built in pure Go.
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：27070 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 91.1k | +434 | 100 | 80.41 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 39.8k | +164 | 100 | 76.10 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.3k | +100 | 100 | 74.93 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.0k | +82 | 100 | 73.75 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.6k | +61 | 100 | 72.38 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +434.0 | +0.48% | 72.91 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +164.0 | +0.41% | 67.15 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +100.0 | +0.19% | 64.45 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +82.0 | +0.23% | 63.21 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +61.0 | +0.23% | 61.47 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38654 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：28162 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：139202 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：78511 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：73290 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 289.4k | +3068 | 100 | 91.07 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 177.4k | +1195 | 100 | 90.68 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 97.8k | +3707 | 100 | 86.40 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 25.5k | +248 | 65 | 79.33 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 266.6k | +5138 | 100 | 76.97 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [agent-skills](https://github.com/addyosmani/agent-skills) | +3707.0 | +3.94% | 84.11 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | +3068.0 | +1.07% | 82.14 |
| 3 | [Anthropic Skills](https://github.com/anthropics/skills) | +1195.0 | +0.68% | 81.36 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +5138.0 | +1.97% | 76.43 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +248.0 | +0.98% | 68.48 |

#### 新发现观察池

- [tt-a1i/archify](https://github.com/tt-a1i/archify)：68467 Stars；匹配度 3；Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.
- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：60519 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：32120 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：139202 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：62481 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.4k | +64 | 100 | 79.90 | Python 官方 SDK |
| 2 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.3k | +63 | 100 | 78.59 | MCP 规范与文档主仓库 |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.4k | +47 | 100 | 78.07 | TypeScript 官方 SDK |
| 4 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.5k | +38 | 100 | 76.07 | 企业工具网关和统一治理 |
| 5 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 90.5k | +207 | 85 | 75.76 | 生态入口不代表每个 Server 均成熟 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | +126.0 | +2.20% | 67.73 |
| 2 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +207.0 | +0.23% | 66.42 |
| 3 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +64.0 | +0.26% | 65.45 |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +63.0 | +0.68% | 65.38 |
| 5 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +47.0 | +0.35% | 63.57 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：95358 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：73290 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57521 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：43926 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：37413 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [A2A](https://github.com/a2aproject/A2A) | 25.9k | +113 | 100 | 81.80 | Agent 到 Agent 的远程互操作 |
| 2 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 16.0k | +90 | 100 | 80.44 | Agent 到 UI 的事件协议 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.9k | +33 | 100 | 67.70 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [A2A](https://github.com/a2aproject/A2A) | +113.0 | +0.44% | 68.70 |
| 2 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +90.0 | +0.57% | 67.40 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +33.0 | +1.17% | 58.36 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：555 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [BrightbeamAI/chap](https://github.com/BrightbeamAI/chap)：103 Stars；匹配度 3；CHAP, the Collaborative Human Agent Protocol, is a MCP/A2A-compatible runtime for auditable human-agent work: approvals, overrides, handoffs, escalation and verifiable evidence logs.
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1455 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：678 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：509 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 32.1k | +501 | 100 | 80.12 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.7k | +36 | 100 | 70.15 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.5k | +164 | 20 | 57.41 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +501.0 | +1.59% | 74.94 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +36.0 | +0.20% | 58.45 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +164.0 | +0.23% | 51.53 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21998 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：107836 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：72954 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：48434 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47059 Stars；匹配度 1；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 15.4k | +258 | 100 | 84.54 | Agent 原生 Sandbox Runtime |
| 2 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 5.3k | +441 | 100 | 84.12 | 无完整容器的 OS 级限制 |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | 13.9k | +113 | 100 | 81.10 | 企业 Agent 云端安全执行环境 |
| 4 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.7k | +115 | 100 | 80.86 | NVIDIA 自主 Agent 安全 Runtime |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 12.6k | +434 | 100 | 80.05 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +441.0 | +9.09% | 87.74 |
| 2 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +434.0 | +3.56% | 77.35 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +258.0 | +1.70% | 74.93 |
| 4 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +133.0 | +3.47% | 70.20 |
| 5 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +115.0 | +1.34% | 69.64 |

#### 新发现观察池

- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2178 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [Augani/dory](https://github.com/Augani/dory)：1593 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1208 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1146 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [Aethena-Lab/Z3r0](https://github.com/Aethena-Lab/Z3r0)：889 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CUA](https://github.com/trycua/cua) | 25.3k | +2685 | 100 | 97.61 | Computer Use 驱动和训练评测平台 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | 115.6k | +1066 | 100 | 90.93 | 浏览器 Agent 主流实现 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 24.7k | +420 | 100 | 86.80 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.7k | +37 | 100 | 69.06 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +11 | 65 | 57.80 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CUA](https://github.com/trycua/cua) | +2685.0 | +11.88% | 98.81 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | +1066.0 | +0.93% | 81.86 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +420.0 | +1.73% | 77.86 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +37.0 | +0.48% | 58.42 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +11.0 | +0.81% | 46.48 |

#### 新发现观察池

- [feder-cr/AIHawk](https://github.com/feder-cr/AIHawk)：31610 Stars；匹配度 3；Anti detect browser and web browsing agent: an open-source MCP server for undetected browsing, AI web scraping and computer use agents. No captchas.
- [microsoft/Webwright](https://github.com/microsoft/Webwright)：6011 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4128 Stars；匹配度 2；Open-source, vision-first browser agent
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1099 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1007 Stars；匹配度 2；Build browser agents for real world tasks

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 59.3k | +608 | 100 | 88.69 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 68.7k | +2855 | 100 | 78.69 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.0k | +63 | 40 | 62.49 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.1k | +13 | 65 | 52.97 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2855.0 | +4.34% | 80.85 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +608.0 | +1.04% | 79.11 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +63.0 | +0.49% | 52.52 |
| 4 | [Plano](https://github.com/katanemo/plano) | +13.0 | +0.18% | 43.69 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：8203 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：5267 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5130 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44163 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：17149 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 34.9k | +309 | 100 | 85.67 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.6k | +112 | 100 | 80.92 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 22.2k | +169 | 100 | 75.52 | 观测评测一体化 |
| 4 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | +13 | 100 | 65.80 | LLM/Agent OTel instrumentation |
| 5 | [OpenLIT](https://github.com/openlit/openlit) | 2.8k | +16 | 100 | 65.06 | AI Engineering 多治理能力 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +309.0 | +0.89% | 74.94 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +112.0 | +0.98% | 69.04 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +169.0 | +0.77% | 67.50 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +16.0 | +0.58% | 53.65 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +13.0 | +0.17% | 52.71 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1541 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：127 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：195 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：144 Stars；匹配度 2；无仓库描述
- [grafana/agento11y](https://github.com/grafana/agento11y)：118 Stars；匹配度 2；Actually Useful Agent Observability

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 25.3k | +241 | 100 | 84.47 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 18.4k | +109 | 100 | 81.26 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.8k | +53 | 100 | 69.77 | 可复现评测任务框架 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.9k | +42 | 100 | 69.19 | 真实代码 Issue 基准 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.8k | +17 | 100 | 66.22 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +241.0 | +0.96% | 73.54 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +109.0 | +0.60% | 68.54 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +53.0 | +1.92% | 62.20 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +42.0 | +0.72% | 59.28 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +17.0 | +0.29% | 54.01 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：375 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：495 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：452 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：330 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：210 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 17.9k | +819 | 100 | 91.23 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.5k | +59 | 100 | 77.80 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.2k | +59 | 100 | 70.61 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 459 | +4 | 20 | 39.19 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +819.0 | +4.78% | 87.07 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +59.0 | +1.32% | 65.70 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +59.0 | +0.83% | 61.37 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +4.0 | +0.88% | 30.74 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：2004 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：568 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)：396 Stars；匹配度 3；Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents. Executable, testable rules for prompt injection, tool poisoning, context exfiltration and MCP attacks. Merged into open-source projects at Microsoft, Cisco, Gen Digital, MISP and FINOS. MIT-licensed.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：322 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：202 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.6k | +65 | 100 | 79.24 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 5.8k | +40 | 100 | 76.50 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.4k | +49 | 100 | 70.81 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Logto](https://github.com/logto-io/logto) | +65.0 | +0.45% | 65.45 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | +40.0 | +0.69% | 62.73 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +49.0 | +0.34% | 60.07 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：66 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [Vorim-AI-Labs/vorim-mcp-server](https://github.com/Vorim-AI-Labs/vorim-mcp-server)：66 Stars；匹配度 3；MCP server for Vorim AI — AI agent identity, permissions, and audit trails. 19 tools for Claude, OpenAI, Cursor, VS Code, and any MCP-compatible client.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8413 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2693 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 37.4k | +98 | 100 | 81.86 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12.2k | +91 | 100 | 72.69 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.6k | +67 | 40 | 62.55 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +98.0 | +0.26% | 67.95 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +91.0 | +0.75% | 63.84 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +67.0 | +0.58% | 52.92 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：797 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：153 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 125.6k | +1666 | 100 | 91.34 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | 208.9k | +1756 | 100 | 90.85 | 终端 Agent 架构参考 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 88.7k | +858 | 100 | 90.33 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 82.8k | +381 | 100 | 87.35 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 247.5k | +2308 | 100 | 83.44 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Codex](https://github.com/openai/codex) | +1666.0 | +1.34% | 82.69 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | +1756.0 | +0.85% | 81.70 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | +858.0 | +0.98% | 81.08 |
| 4 | [herdr](https://github.com/herdrdev/herdr) | +1630.0 | +4.26% | 80.22 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +2308.0 | +0.94% | 78.13 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：26931 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：263966 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：77302 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：72954 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47058 Stars；匹配度 2；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
