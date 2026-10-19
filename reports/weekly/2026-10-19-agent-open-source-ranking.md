# AI Agent 开源项目周榜（2026-10-19）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-10-12，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 43.5k | +377 | 100 | 86.61 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 30.1k | +148 | 100 | 82.90 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Google ADK Python](https://github.com/google/adk-python) | 21.9k | +124 | 100 | 81.91 | 企业 Agent 生命周期覆盖完整 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 14.2k | +133 | 100 | 81.74 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 59.9k | +266 | 100 | 78.23 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +377.0 | +0.87% | 76.10 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +148.0 | +0.49% | 70.30 |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | +266.0 | +0.45% | 70.01 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +133.0 | +0.95% | 70.01 |
| 5 | [Google ADK Python](https://github.com/google/adk-python) | +124.0 | +0.57% | 69.28 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1892 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：878 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：7005 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4569 Stars；匹配度 2；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3820 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 23.8k | +199 | 100 | 83.69 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.6k | +27 | 100 | 67.38 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +18 | 100 | 64.99 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +199.0 | +0.84% | 72.28 |
| 2 | [Restate](https://github.com/restatedev/restate) | +27.0 | +0.59% | 56.64 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +18.0 | +1.11% | 54.82 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1252 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：8139 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：136 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.
- [kkjiangk/agent-py](https://github.com/kkjiangk/agent-py)：101 Stars；匹配度 2；Personal AIOps engineering project with durable workflows, scoped hybrid retrieval, reliable event delivery, and verified API/browser contracts.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | 30.8k | +4100 | 100 | 97.96 | 独立 Context Manager 的直接样本 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | 40.3k | +576 | 100 | 88.28 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 49.6k | +150 | 40 | 74.61 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 36.3k | +65 | 100 | 73.05 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.8k | +19 | 100 | 58.15 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | +4100.0 | +15.34% | 98.98 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | +576.0 | +1.45% | 79.33 |
| 3 | [Continue](https://github.com/continuedev/continue) | +65.0 | +0.18% | 61.96 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +150.0 | +0.30% | 61.42 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +19.0 | +0.68% | 50.94 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：101660 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79315 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [upstash/context7](https://github.com/upstash/context7)：63265 Stars；匹配度 2；Context7 Platform -- Up-to-date docs for AI agents
- [PostHog/posthog](https://github.com/PostHog/posthog)：40340 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：28632 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 67.4k | +397 | 100 | 87.24 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 32.5k | +443 | 100 | 87.08 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 25.2k | +72 | 100 | 80.31 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 11.9k | +104 | 100 | 73.16 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 29.7k | +334 | 100 | 70.86 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Cognee](https://github.com/topoteretes/cognee) | +443.0 | +1.38% | 77.67 |
| 2 | [Mem0](https://github.com/mem0ai/mem0) | +397.0 | +0.59% | 76.17 |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | +334.0 | +1.14% | 68.18 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +72.0 | +0.29% | 66.11 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +104.0 | +0.88% | 64.74 |

#### 新发现观察池

- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：4301 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1281 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1109 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：51322 Stars；匹配度 2；Hindsight: Agent Memory That Learns
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：29592 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 92.4k | +416 | 100 | 80.28 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 40.2k | +127 | 100 | 75.28 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.6k | +94 | 100 | 74.75 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.4k | +85 | 100 | 73.87 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.8k | +51 | 100 | 71.84 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +416.0 | +0.45% | 72.65 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +127.0 | +0.32% | 65.68 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +94.0 | +0.18% | 64.12 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +85.0 | +0.23% | 63.41 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +51.0 | +0.19% | 60.51 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38695 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：34645 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：142244 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79315 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：76666 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 301.7k | +3875 | 100 | 91.30 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 182.0k | +1465 | 100 | 90.81 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 108.3k | +3102 | 100 | 85.45 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 26.3k | +224 | 65 | 78.97 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 296.5k | +9753 | 100 | 78.40 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Superpowers](https://github.com/obra/superpowers) | +3875.0 | +1.30% | 82.60 |
| 2 | [agent-skills](https://github.com/addyosmani/agent-skills) | +3102.0 | +2.95% | 82.15 |
| 3 | [Anthropic Skills](https://github.com/anthropics/skills) | +1465.0 | +0.81% | 81.62 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +9753.0 | +3.40% | 79.30 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +224.0 | +0.86% | 67.75 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：69600 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：35525 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：142244 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)：98952 Stars；匹配度 2；Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages
- [tt-a1i/archify](https://github.com/tt-a1i/archify)：85490 Stars；匹配度 2；Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.6k | +66 | 100 | 80.01 | Python 官方 SDK |
| 2 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.6k | +53 | 100 | 78.48 | TypeScript 官方 SDK |
| 3 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 91.4k | +202 | 100 | 77.95 | 生态入口不代表每个 Server 均成熟 |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.5k | +46 | 100 | 77.54 | MCP 规范与文档主仓库 |
| 5 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.7k | +49 | 100 | 77.06 | 企业工具网关和统一治理 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +202.0 | +0.22% | 68.54 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +66.0 | +0.27% | 65.62 |
| 3 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | +49.0 | +1.06% | 64.29 |
| 4 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +53.0 | +0.39% | 64.26 |
| 5 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +46.0 | +0.49% | 63.44 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：96584 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：75924 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57593 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：46877 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 162 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：38351 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 16.7k | +212 | 100 | 83.70 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 26.2k | +88 | 100 | 81.01 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 3.0k | +32 | 85 | 65.36 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +212.0 | +1.29% | 73.18 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +88.0 | +0.34% | 67.25 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +32.0 | +1.09% | 55.84 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：552 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [openJiuwen-ai/agent-protocol](https://github.com/openJiuwen-ai/agent-protocol)：115 Stars；匹配度 3；openJiuwen agent-protocol provides implementations of agent communication protocols, including C++ SDKs for MCP and A2A protocols.
- [BrightbeamAI/chap](https://github.com/BrightbeamAI/chap)：110 Stars；匹配度 3；CHAP, the Collaborative Human Agent Protocol, is a MCP/A2A-compatible runtime for auditable human-agent work: approvals, overrides, handoffs, escalation and verifiable evidence logs.
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1460 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：688 Stars；匹配度 2；无仓库描述

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 33.5k | +375 | 100 | 78.90 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.9k | +61 | 100 | 71.81 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70.9k | +104 | 20 | 56.02 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +375.0 | +1.13% | 72.61 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +61.0 | +0.34% | 61.35 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +104.0 | +0.15% | 49.08 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：22062 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：111959 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：76666 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：49161 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47460 Stars；匹配度 1；Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 16.6k | +756 | 100 | 90.84 | NVIDIA 自主 Agent 安全 Runtime |
| 2 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 5.6k | +736 | 100 | 86.61 | 无完整容器的 OS 级限制 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 16.0k | +168 | 100 | 82.73 | Agent 原生 Sandbox Runtime |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | 14.4k | +149 | 100 | 82.19 | 企业 Agent 云端安全执行环境 |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 13.0k | +91 | 100 | 72.75 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +736.0 | +15.17% | 92.20 |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +756.0 | +4.76% | 86.55 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +168.0 | +1.06% | 71.53 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +149.0 | +1.04% | 70.79 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +82.0 | +1.94% | 64.79 |

#### 新发现观察池

- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4569 Stars；匹配度 3；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2311 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [Augani/dory](https://github.com/Augani/dory)：1627 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1588 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1197 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 118.4k | +769 | 100 | 89.90 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 30.2k | +748 | 100 | 89.62 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 25.7k | +97 | 100 | 81.30 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.8k | +47 | 100 | 69.89 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +9 | 100 | 62.41 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CUA](https://github.com/trycua/cua) | +748.0 | +2.54% | 82.58 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | +769.0 | +0.65% | 79.98 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +97.0 | +0.38% | 67.81 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +47.0 | +0.60% | 59.86 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +9.0 | +0.64% | 50.50 |

#### 新发现观察池

- [Agenta-AI/awesome-ai-agent-platforms](https://github.com/Agenta-AI/awesome-ai-agent-platforms)：562 Stars；匹配度 3；A curated list of open-source AI agent platforms: AI coworkers and teammates, agent builders and frameworks, workflow automation platforms, browser agents, and coding agents, with licenses.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4134 Stars；匹配度 2；Open-source, vision-first browser agent
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1496 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1006 Stars；匹配度 2；Build browser agents for real world tasks
- [outcrawlai/scout](https://github.com/outcrawlai/scout)：946 Stars；匹配度 2；Scout: the open-source browser agent, by Outcrawl. Mirrored automatically from Outcrawl's own repository.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 61.5k | +519 | 100 | 88.11 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 78.2k | +2789 | 100 | 78.27 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.2k | +45 | 40 | 61.41 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.1k | +7 | 100 | 56.52 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2789.0 | +3.70% | 79.68 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +519.0 | +0.85% | 77.97 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +45.0 | +0.34% | 50.57 |
| 4 | [Plano](https://github.com/katanemo/plano) | +7.0 | +0.10% | 45.94 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：8923 Stars；匹配度 3；Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-compatible API for 10,000+ models, with failover, load balancing, semantic caching, virtual keys, budgets and MCP Code Mode. Works with any SDK or agent and adds under 200µs of overhead at 5k RPS.
- [TykTechnologies/tyk](https://github.com/TykTechnologies/tyk)：10865 Stars；匹配度 2；Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol)
- [looplj/axonhub](https://github.com/looplj/axonhub)：5367 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5215 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：44278 Stars；匹配度 1；🦍 The API and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 36.0k | +333 | 100 | 85.98 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.9k | +107 | 100 | 80.77 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 22.7k | +204 | 100 | 76.24 | 观测评测一体化 |
| 4 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.5k | +17 | 100 | 66.60 | LLM/Agent OTel instrumentation |
| 5 | [OpenLIT](https://github.com/openlit/openlit) | 2.9k | +16 | 100 | 65.09 | AI Engineering 多治理能力 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +333.0 | +0.93% | 75.42 |
| 2 | [Opik](https://github.com/comet-ml/opik) | +204.0 | +0.91% | 68.75 |
| 3 | [Phoenix](https://github.com/Arize-ai/phoenix) | +107.0 | +0.91% | 68.69 |
| 4 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +17.0 | +0.23% | 54.10 |
| 5 | [OpenLIT](https://github.com/openlit/openlit) | +16.0 | +0.56% | 53.64 |

#### 新发现观察池

- [langwatch/langwatch](https://github.com/langwatch/langwatch)：4977 Stars；匹配度 3；Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company.
- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1548 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：127 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：192 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：147 Stars；匹配度 2；无仓库描述

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 26.1k | +213 | 100 | 84.03 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 18.9k | +187 | 100 | 83.27 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 3.0k | +55 | 100 | 69.93 | 可复现评测任务框架 |
| 4 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.9k | +22 | 100 | 67.04 | Agent Evaluation 与 Testing |
| 5 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 6.0k | +44 | 65 | 64.13 | 真实代码 Issue 基准 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +213.0 | +0.82% | 72.67 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +187.0 | +1.00% | 72.08 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +55.0 | +1.84% | 62.30 |
| 4 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +22.0 | +0.37% | 55.43 |
| 5 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +44.0 | +0.73% | 54.32 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：376 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：576 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：449 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：332 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：209 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 20.5k | +521 | 100 | 87.97 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.6k | +45 | 100 | 76.73 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.3k | +47 | 100 | 69.81 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 472 | +3 | 20 | 38.35 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +521.0 | +2.61% | 80.54 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +45.0 | +0.98% | 63.69 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +47.0 | +0.65% | 59.89 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +3.0 | +0.64% | 29.15 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：2021 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：585 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)：418 Stars；匹配度 3；Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents. Executable, testable rules for prompt injection, tool poisoning, context exfiltration and MCP attacks. Merged into open-source projects at Microsoft, Cisco, Gen Digital, MISP and FINOS. MIT-licensed.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：341 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：203 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | 6.0k | +46 | 100 | 77.03 | Agent/Skill/Tool/Resource 关系授权 |
| 2 | [Logto](https://github.com/logto-io/logto) | 14.7k | +18 | 100 | 75.32 | AI App 身份认证与授权底座 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.6k | +51 | 100 | 70.95 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | +46.0 | +0.77% | 63.61 |
| 2 | [Casdoor](https://github.com/casdoor/casdoor) | +51.0 | +0.35% | 60.30 |
| 3 | [Logto](https://github.com/logto-io/logto) | +18.0 | +0.12% | 58.50 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：67 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8405 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2685 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [VibeTensor/attestix](https://github.com/VibeTensor/attestix)：874 Stars；匹配度 2；AI agent identity, signed credentials, delegated authority and portable governance evidence. Python core and offline verifier SDKs.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38.1k | +149 | 100 | 83.22 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12.6k | +114 | 100 | 73.55 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.7k | +15 | 100 | 66.93 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +149.0 | +0.39% | 70.33 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +114.0 | +0.91% | 65.32 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +15.0 | +0.13% | 53.69 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：795 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | 216.8k | +4050 | 100 | 91.90 | 终端 Agent 架构参考 |
| 2 | [Codex](https://github.com/openai/codex) | 129.8k | +1088 | 100 | 90.85 | 完整 Coding Agent Harness 源码样本 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 91.2k | +584 | 100 | 88.93 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 84.1k | +375 | 100 | 87.31 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 255.0k | +2122 | 100 | 83.34 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | +4050.0 | +1.90% | 83.81 |
| 2 | [Codex](https://github.com/openai/codex) | +1088.0 | +0.85% | 81.69 |
| 3 | [Paperclip](https://github.com/paperclipai/paperclip) | +3736.0 | +3.72% | 79.93 |
| 4 | [OpenHands](https://github.com/OpenHands/OpenHands) | +584.0 | +0.64% | 78.49 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +2122.0 | +0.84% | 77.93 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：27453 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [1jehuang/jcode](https://github.com/1jehuang/jcode)：21017 Stars；匹配度 3；High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- [zai-org/ZCode](https://github.com/zai-org/ZCode)：7943 Stars；匹配度 3；Z.ai's coding agent harness. Powerful, intelligent, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：283430 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：78799 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
