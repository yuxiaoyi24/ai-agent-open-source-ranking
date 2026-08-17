# AI Agent 开源项目周榜（2026-08-17）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-08-10，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 39.8k | +476 | 100 | 87.47 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 28.7k | +173 | 100 | 83.37 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 12.8k | +132 | 100 | 81.63 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 21.1k | +91 | 100 | 80.83 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 57.2k | +291 | 100 | 78.48 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +476.0 | +1.21% | 77.87 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +173.0 | +0.61% | 71.27 |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | +291.0 | +0.51% | 70.55 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +132.0 | +1.04% | 70.07 |
| 5 | [Google ADK Python](https://github.com/google/adk-python) | +91.0 | +0.43% | 67.43 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1894 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：856 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [swarmclawai/swarmclaw](https://github.com/swarmclawai/swarmclaw)：648 Stars；匹配度 3；Open-source self-hosted AI agent runtime and multi-agent framework for autonomous agent swarms. Agent memory, MCP tools, schedules, delegation, and 23+ LLM providers (Claude, GPT, Gemini, OpenRouter, Ollama). A practical Claude Code and LangChain alternative.
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork)：4053 Stars；匹配度 2；A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [google/ax](https://github.com/google/ax)：1956 Stars；匹配度 2；An open source distributed agent runtime

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 22.3k | +142 | 100 | 82.41 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.3k | +32 | 100 | 67.91 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.5k | +13 | 100 | 63.74 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +142.0 | +0.64% | 70.12 |
| 2 | [Restate](https://github.com/restatedev/restate) | +32.0 | +0.75% | 57.73 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +13.0 | +0.86% | 52.70 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1234 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7729 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 28.7k | +544 | 100 | 88.01 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 19.9k | +154 | 100 | 82.58 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 48.3k | +186 | 65 | 79.02 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 35.5k | +84 | 100 | 73.80 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.5k | +49 | 100 | 61.91 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | +544.0 | +1.93% | 79.71 |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | +154.0 | +0.78% | 70.71 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | +186.0 | +0.39% | 66.40 |
| 4 | [Continue](https://github.com/continuedev/continue) | +84.0 | +0.24% | 63.33 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +49.0 | +1.97% | 58.07 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：90915 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77506 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：37712 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：27427 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：26203 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Install from npm, the Claude Code plugin marketplace, or npx skills. Codex, Cursor, OpenCode, 60+ agents.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 63.4k | +483 | 100 | 87.87 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 30.1k | +167 | 100 | 83.31 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.3k | +105 | 100 | 81.48 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 10.7k | +72 | 100 | 71.72 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 27.1k | +274 | 100 | 70.02 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +483.0 | +0.77% | 77.46 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +167.0 | +0.56% | 71.04 |
| 3 | [Letta](https://github.com/letta-ai/letta) | +105.0 | +0.43% | 68.27 |
| 4 | [agentmemory](https://github.com/rohitg00/agentmemory) | +274.0 | +1.02% | 66.87 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +72.0 | +0.68% | 62.40 |

#### 新发现观察池

- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1162 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：883 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)：659 Stars；匹配度 3；The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：22263 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：20048 Stars；匹配度 2；Hindsight: Agent Memory That  Learns

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 88.6k | +1460 | 100 | 83.97 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 38.9k | +200 | 100 | 76.73 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 51.7k | +162 | 100 | 76.42 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 35.5k | +158 | 100 | 75.82 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.2k | +63 | 100 | 72.46 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +1460.0 | +1.68% | 79.50 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +200.0 | +0.52% | 68.33 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +162.0 | +0.31% | 67.11 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +158.0 | +0.45% | 66.93 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +63.0 | +0.24% | 61.64 |

#### 新发现观察池

- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)：45448 Stars；匹配度 4；GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a git repository (Github, Gitlab, Azure, Local) or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration
- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38545 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：19928 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：132899 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77506 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Anthropic Skills](https://github.com/anthropics/skills) | 169.8k | +2472 | 100 | 91.48 | 官方 Skill 样本库 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | 272.8k | +2948 | 100 | 91.09 | Skill 驱动的软件工程方法 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 87.8k | +2436 | 100 | 85.13 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 24.3k | +270 | 100 | 84.89 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 219.4k | +7699 | 100 | 78.64 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Anthropic Skills](https://github.com/anthropics/skills) | +2472.0 | +1.48% | 82.96 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | +2948.0 | +1.09% | 82.18 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | +2436.0 | +2.85% | 81.85 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +7699.0 | +3.64% | 79.77 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +270.0 | +1.12% | 74.40 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：48391 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [googleworkspace/cli](https://github.com/googleworkspace/cli)：30412 Stars；匹配度 3；Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：29033 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：132899 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：58406 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.0k | +68 | 100 | 80.07 | Python 官方 SDK |
| 2 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.2k | +73 | 100 | 79.50 | TypeScript 官方 SDK |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.0k | +69 | 100 | 78.89 | MCP 规范与文档主仓库 |
| 4 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 89.6k | +223 | 100 | 78.23 | 生态入口不代表每个 Server 均成熟 |
| 5 | [Open Connector](https://github.com/oomol-lab/open-connector) | 4.7k | +231 | 100 | 78.10 | 1000+ SaaS 的认证连接网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Open Connector](https://github.com/oomol-lab/open-connector) | +231.0 | +5.13% | 76.46 |
| 2 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +223.0 | +0.25% | 69.07 |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +73.0 | +0.56% | 66.16 |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +69.0 | +0.78% | 65.98 |
| 5 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +68.0 | +0.28% | 65.78 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：92449 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：66541 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57447 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：39152 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：36187 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 15.3k | +130 | 100 | 81.71 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 25.4k | +101 | 100 | 81.41 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.7k | +27 | 100 | 66.89 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +130.0 | +0.85% | 69.78 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +101.0 | +0.40% | 68.04 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +27.0 | +1.00% | 57.01 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：551 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1457 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：651 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：506 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support
- [mahonzhan/awesome-agent-harness](https://github.com/mahonzhan/awesome-agent-harness)：257 Stars；匹配度 2；A curated awesome list of agent harnesses, agent frameworks, workflow frameworks, and emerging agent protocols.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 29.0k | +222 | 100 | 76.78 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.6k | +22 | 100 | 68.68 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 69.9k | +105 | 20 | 56.03 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +222.0 | +0.77% | 69.12 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +22.0 | +0.13% | 55.88 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +105.0 | +0.15% | 49.12 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21905 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：98515 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：68018 Stars；匹配度 1；🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：47067 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)：42108 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 14.0k | +1537 | 100 | 96.58 | Agent 原生 Sandbox Runtime |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.2k | +146 | 100 | 81.92 | NVIDIA 自主 Agent 安全 Runtime |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | 13.4k | +98 | 100 | 80.55 | 企业 Agent 云端安全执行环境 |
| 4 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 11.2k | +136 | 100 | 74.17 | 国内高并发轻量 Sandbox 路线 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 3.5k | +79 | 100 | 71.67 | K8s 上 Agent 隔离工作负载 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +1537.0 | +12.37% | 98.29 |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +146.0 | +1.81% | 71.74 |
| 3 | [E2B](https://github.com/e2b-dev/E2B) | +98.0 | +0.74% | 68.01 |
| 4 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +136.0 | +1.23% | 66.74 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +79.0 | +2.28% | 65.12 |

#### 新发现观察池

- [pullrun/pullrun](https://github.com/pullrun/pullrun)：123 Stars；匹配度 3；The AI agent sandbox runtime. Boot any OCI image as a Firecracker microVM, Linux container, or Apple Silicon VM in ~400 ms — zero-copy DAG storage, P2P image sync, native MCP for opencode/Claude Code/Cursor.
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：1980 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1090 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：683 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [yv1ing/Z3r0](https://github.com/yv1ing/Z3r0)：618 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 109.4k | +902 | 100 | 90.54 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 21.4k | +353 | 100 | 85.99 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 24.0k | +166 | 100 | 83.03 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.5k | +37 | 100 | 69.03 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.3k | +7 | 65 | 56.29 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | +902.0 | +0.83% | 81.15 |
| 2 | [CUA](https://github.com/trycua/cua) | +353.0 | +1.68% | 76.75 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +166.0 | +0.70% | 71.09 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +37.0 | +0.50% | 58.42 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +7.0 | +0.53% | 43.84 |

#### 新发现观察池

- [microsoft/Webwright](https://github.com/microsoft/Webwright)：5918 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4115 Stars；匹配度 2；Open-source, vision-first browser agent
- [oxylabs/browser-agent-py](https://github.com/oxylabs/browser-agent-py)：1489 Stars；匹配度 2；AI Browser Agent is an advanced Browser AI tool developed by Oxylabs AI Studio that automates real user browsing tasks using natural language instructions.
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1010 Stars；匹配度 2；Build browser agents for real world tasks
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：783 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 56.5k | +490 | 100 | 87.82 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 49.2k | +4659 | 100 | 83.77 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 12.7k | +66 | 65 | 66.37 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.0k | +7 | 100 | 56.50 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +4659.0 | +10.46% | 91.88 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +490.0 | +0.88% | 77.65 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +66.0 | +0.52% | 56.56 |
| 4 | [Plano](https://github.com/katanemo/plano) | +7.0 | +0.10% | 45.93 |

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：7347 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：4997 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：3316 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.
- [Kong/kong](https://github.com/Kong/kong)：43989 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：17000 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 33.2k | +411 | 100 | 86.77 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 11.1k | +107 | 100 | 80.71 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 21.4k | +155 | 100 | 75.17 | 观测评测一体化 |
| 4 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | +13 | 100 | 65.79 | LLM/Agent OTel instrumentation |
| 5 | [OpenLIT](https://github.com/openlit/openlit) | 2.7k | +14 | 100 | 64.58 | AI Engineering 多治理能力 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +411.0 | +1.25% | 77.06 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +107.0 | +0.98% | 68.76 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +155.0 | +0.73% | 66.96 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +14.0 | +0.52% | 52.88 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +13.0 | +0.18% | 52.71 |

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1516 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：136 Stars；匹配度 2；无仓库描述
- [dreadnode/agent-lens](https://github.com/dreadnode/agent-lens)：114 Stars；匹配度 2；Agent observability and replay tooling for AI safety & interpretability research.

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 24.3k | +191 | 100 | 83.56 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 17.6k | +130 | 100 | 81.84 | LLM/Agent Evaluation Framework |
| 3 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 5.6k | +46 | 100 | 69.48 | 真实代码 Issue 基准 |
| 4 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.6k | +48 | 100 | 69.31 | 可复现评测任务框架 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.8k | +13 | 100 | 65.41 | Agent Evaluation 与 Testing |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +191.0 | +0.79% | 71.99 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +130.0 | +0.74% | 69.68 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +48.0 | +1.91% | 61.61 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +46.0 | +0.82% | 59.90 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +13.0 | +0.23% | 52.59 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：370 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：493 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：327 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [h9-tec/llm-systems-engineering-roadmap](https://github.com/h9-tec/llm-systems-engineering-roadmap)：181 Stars；匹配度 3；A practical roadmap for mastering LLM internals, training, inference, RAG, agents, evaluation, and production architecture.
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：161 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 14.7k | +237 | 100 | 84.15 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.3k | +41 | 100 | 76.32 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.0k | +63 | 100 | 70.83 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 445 | +4 | 20 | 39.16 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +237.0 | +1.64% | 74.34 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +41.0 | +0.96% | 63.13 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +63.0 | +0.91% | 61.83 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +4.0 | +0.91% | 30.77 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：1966 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：539 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：295 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：196 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work
- [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)：3003 Stars；匹配度 2；Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.4k | +40 | 100 | 77.66 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 5.6k | +36 | 100 | 76.10 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.2k | +50 | 100 | 70.85 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Logto](https://github.com/logto-io/logto) | +40.0 | +0.28% | 62.69 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | +36.0 | +0.65% | 62.09 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +50.0 | +0.35% | 60.18 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：56 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8544 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2703 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity)：1201 Stars；匹配度 2；多线程全自动注册free 绕过接码使用codex
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：755 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 36.8k | +129 | 100 | 82.71 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 11.7k | +164 | 100 | 74.98 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.3k | +66 | 65 | 66.22 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +129.0 | +0.35% | 69.50 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +164.0 | +1.42% | 68.10 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +66.0 | +0.59% | 56.59 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：794 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：152 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | 198.1k | +2585 | 100 | 91.32 | 终端 Agent 架构参考 |
| 2 | [Codex](https://github.com/openai/codex) | 106.3k | +1252 | 100 | 91.19 | 完整 Coding Agent Harness 源码样本 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 84.2k | +655 | 100 | 89.27 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 80.1k | +471 | 100 | 88.03 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 231.6k | +3477 | 100 | 84.02 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [herdr](https://github.com/herdrdev/herdr) | +3141.0 | +11.79% | 91.45 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | +2585.0 | +1.32% | 82.64 |
| 3 | [Codex](https://github.com/openai/codex) | +1252.0 | +1.19% | 82.38 |
| 4 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +3477.0 | +1.52% | 79.30 |
| 5 | [OpenHands](https://github.com/OpenHands/OpenHands) | +655.0 | +0.78% | 79.28 |

#### 新发现观察池

- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)：67961 Stars；匹配度 3；omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- [xai-org/grok-build](https://github.com/xai-org/grok-build)：25397 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：240507 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：74394 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：46528 Stars；匹配度 2；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
