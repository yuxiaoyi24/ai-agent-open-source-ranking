# AI Agent 开源项目周榜（2026-08-05）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 当前为首期基线，没有上一期快照；增长榜暂不代表真实周增量。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 38.9k | — | 100 | 97.13 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 28.4k | — | 100 | 96.17 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Google ADK Python](https://github.com/google/adk-python) | 21.0k | — | 100 | 95.26 | 企业 Agent 生命周期覆盖完整 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 12.6k | — | 100 | 93.70 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 56.6k | — | 100 | 88.27 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1920 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：846 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [swarmclawai/swarmclaw](https://github.com/swarmclawai/swarmclaw)：634 Stars；匹配度 3；Open-source self-hosted AI agent runtime and multi-agent framework for autonomous agent swarms. Agent memory, MCP tools, schedules, delegation, and 23+ LLM providers (Claude, GPT, Gemini, OpenRouter, Ollama). A practical Claude Code and LangChain alternative.
- [google/ax](https://github.com/google/ax)：1924 Stars；匹配度 2；An open source distributed agent runtime
- [GCWing/BitFun](https://github.com/GCWing/BitFun)：1456 Stars；匹配度 2；BitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 22.1k | — | 100 | 95.41 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.3k | — | 100 | 80.40 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.5k | — | 100 | 77.26 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1225 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：7668 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 28.0k | — | 100 | 96.13 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 19.6k | — | 100 | 95.05 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 47.9k | — | 65 | 90.77 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 35.3k | — | 85 | 83.84 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.5k | — | 100 | 68.73 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：89655 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77275 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [PostHog/posthog](https://github.com/PostHog/posthog)：37505 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：27116 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)：25984 Stars；匹配度 2；Persistent file-based planning for AI coding agents and long-running tasks. Crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-injection against context rot, deterministic completion gate. Manus-style. Claude Code, Codex, Cursor, Kiro, OpenCode and 60+ agents via the Agent Skills standard.

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 62.6k | — | 100 | 98.57 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 29.8k | — | 100 | 96.32 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 24.1k | — | 100 | 95.67 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 10.6k | — | 100 | 83.18 | 自演进 Memory OS 路线 |
| 5 | [Zep](https://github.com/getzep/zep) | 4.8k | — | 100 | 80.78 | 当前公开仓库偏示例集成需核验开源边界 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1136 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：839 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)：642 Stars；匹配度 3；The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：19116 Stars；匹配度 2；Hindsight: Agent Memory That  Learns
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：14527 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 86.9k | — | 100 | 89.57 | 完整 RAG 工程链和 Context Layer |
| 2 | [LlamaIndex](https://github.com/run-llama/llama_index) | 51.4k | — | 100 | 87.98 | 文档和数据 Agent 基础栈 |
| 3 | [LightRAG](https://github.com/HKUDS/LightRAG) | 38.5k | — | 100 | 87.10 | 轻量图 RAG 和增量更新 |
| 4 | [Haystack](https://github.com/deepset-ai/haystack) | 26.1k | — | 100 | 85.92 | 显式可控的 Context/RAG Pipeline |
| 5 | [GraphRAG](https://github.com/microsoft/graphrag) | 35.3k | — | 85 | 83.83 | 图谱社区摘要与检索 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)：45087 Stars；匹配度 4；GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a git repository (Github, Gitlab, Azure, Local) or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration
- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38508 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain 
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：19393 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：130677 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：77275 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 266.9k | — | 100 | 100.00 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 166.4k | — | 100 | 100.00 | 官方 Skill 样本库 |
| 3 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 23.9k | — | 100 | 95.65 | Skill 可移植规范 |
| 4 | [agent-skills](https://github.com/addyosmani/agent-skills) | 81.7k | — | 100 | 89.39 | 生产级编码 Skill 样本 |
| 5 | [Composio](https://github.com/ComposioHQ/composio) | 29.5k | — | 100 | 86.29 | 工具生态和认证执行一体化 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：45219 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [googleworkspace/cli](https://github.com/googleworkspace/cli)：30206 Stars；匹配度 3；Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：28075 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：130677 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：57312 Stars；匹配度 2；AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 23.9k | — | 100 | 95.65 | Python 官方 SDK |
| 2 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.1k | — | 100 | 93.82 | TypeScript 官方 SDK |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 8.9k | — | 100 | 92.63 | MCP 规范与文档主仓库 |
| 4 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.2k | — | 100 | 90.40 | 企业工具网关和统一治理 |
| 5 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 89.2k | — | 100 | 89.65 | 生态入口不代表每个 Server 均成熟 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：91844 Stars；匹配度 2；A collection of MCP servers.
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：64910 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57405 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)：37550 Stars；匹配度 2；High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：35821 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [A2A](https://github.com/a2aproject/A2A) | 25.2k | — | 100 | 95.81 | Agent 到 Agent 的远程互操作 |
| 2 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 15.1k | — | 100 | 94.26 | Agent 到 UI 的事件协议 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 2.7k | — | 100 | 79.00 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：551 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1458 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.
- [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol)：644 Stars；匹配度 2；无仓库描述
- [OTA-Tech-AI/web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)：505 Stars；匹配度 2；🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support
- [mahonzhan/awesome-agent-harness](https://github.com/mahonzhan/awesome-agent-harness)：245 Stars；匹配度 2；A curated awesome list of agent harnesses, agent frameworks, workflow frameworks, and emerging agent protocols.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 28.6k | — | 100 | 86.19 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 17.5k | — | 100 | 84.71 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 69.7k | — | 20 | 62.90 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：21877 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：95668 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：67074 Stars；匹配度 1；🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：46651 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)：41683 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [E2B](https://github.com/e2b-dev/E2B) | 13.3k | — | 100 | 93.86 | 企业 Agent 云端安全执行环境 |
| 2 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 12.4k | — | 100 | 93.64 | Agent 原生 Sandbox Runtime |
| 3 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 8.0k | — | 100 | 92.32 | NVIDIA 自主 Agent 安全 Runtime |
| 4 | [Daytona](https://github.com/daytonaio/daytona) | 72.1k | — | 65 | 92.00 | AI 生成代码的安全弹性执行 |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 10.9k | — | 100 | 83.26 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：1878 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1069 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.
- [ccfos/huatuo](https://github.com/ccfos/huatuo)：1052 Stars；匹配度 2；eBPF-based observability for Linux kernel & Agent sandbox 🚀🚀
- [yv1ing/Z3r0](https://github.com/yv1ing/Z3r0)：608 Stars；匹配度 2；AI-native red-team workbench for authorized penetration testing and vulnerability research, with specialist agents, sandboxed tooling, evidence records, and replayable timelines.
- [h5i-dev/h5i](https://github.com/h5i-dev/h5i)：502 Stars；匹配度 2；Auditable workspaces for AI coding agents: sandboxed worktrees, programmable multi-agent orchestration, automated security checks, up to 95% less token waste, and persistent memory.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 107.9k | — | 100 | 100.00 | 浏览器 Agent 主流实现 |
| 2 | [Stagehand](https://github.com/browserbase/stagehand) | 23.7k | — | 100 | 95.63 | 确定性浏览器 API 与 Agent 结合 |
| 3 | [CUA](https://github.com/trycua/cua) | 20.9k | — | 100 | 95.25 | Computer Use 驱动和训练评测平台 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.4k | — | 85 | 79.09 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.3k | — | 40 | 64.81 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [microsoft/Webwright](https://github.com/microsoft/Webwright)：5883 Stars；匹配度 2；A simple SWE style browser agent framework that achieves SOTA results on long horizon web tasks. 
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4108 Stars；匹配度 2；Open-source, vision-first browser agent
- [oxylabs/browser-agent-py](https://github.com/oxylabs/browser-agent-py)：1415 Stars；匹配度 2；AI Browser Agent is an advanced Browser AI tool developed by Oxylabs AI Studio that automates real user browsing tasks using natural language instructions.
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1010 Stars；匹配度 2；Build browser agents for real world tasks
- [LvcidPsyche/auto-browser](https://github.com/LvcidPsyche/auto-browser)：751 Stars；匹配度 2；Give your AI agent a real browser — with a human in the loop. Open-source MCP-native browser agent.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 55.6k | — | 100 | 98.22 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 40.1k | — | 100 | 77.23 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 12.6k | — | 65 | 76.71 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.0k | — | 100 | 71.90 | Agentic App Data Plane |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [maximhq/bifrost](https://github.com/maximhq/bifrost)：7064 Stars；匹配度 3；Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
- [looplj/axonhub](https://github.com/looplj/axonhub)：4881 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [Kong/kong](https://github.com/Kong/kong)：43921 Stars；匹配度 1；🦍 The API and AI Gateway
- [apache/apisix](https://github.com/apache/apisix)：16958 Stars；匹配度 1；The Cloud-Native API Gateway and AI Gateway
- [InsForge/InsForge](https://github.com/InsForge/InsForge)：12651 Stars；匹配度 1；The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, storage, compute, hosting, and AI gateway to ship full-stack apps end-to-end.

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 32.6k | — | 100 | 96.59 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 10.9k | — | 100 | 93.26 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 21.1k | — | 100 | 85.27 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.7k | — | 100 | 78.99 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.4k | — | 65 | 75.07 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1508 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：134 Stars；匹配度 2；无仓库描述
- [dreadnode/agent-lens](https://github.com/dreadnode/agent-lens)：111 Stars；匹配度 2；Agent observability and replay tooling for AI safety & interpretability research.

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 23.9k | — | 100 | 95.65 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 17.4k | — | 100 | 94.69 | LLM/Agent Evaluation Framework |
| 3 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.7k | — | 100 | 81.31 | Agent Evaluation 与 Testing |
| 4 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.5k | — | 100 | 78.76 | 可复现评测任务框架 |
| 5 | [OpenEvals](https://github.com/langchain-ai/openevals) | 1.1k | — | 100 | 76.43 | 现成 Evaluator 和轨迹评测 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：370 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：548 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：327 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [h9-tec/llm-systems-engineering-roadmap](https://github.com/h9-tec/llm-systems-engineering-roadmap)：175 Stars；匹配度 3；A practical roadmap for mastering LLM internals, training, inference, RAG, agents, evaluation, and production architecture.
- [Infinity-AILab/DeepResearchEval](https://github.com/Infinity-AILab/DeepResearchEval)：142 Stars；匹配度 3；DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation.

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 14.2k | — | 100 | 94.07 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.2k | — | 100 | 90.40 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 6.9k | — | 100 | 81.86 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 438 | — | 20 | 47.50 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：1953 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：511 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：265 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：193 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work
- [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)：2969 Stars；匹配度 2；Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.3k | — | 100 | 94.08 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 5.5k | — | 100 | 91.21 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.1k | — | 100 | 84.05 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：53 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities. Open source.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8553 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2566 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity)：1174 Stars；匹配度 2；多线程全自动注册free 绕过接码使用codex
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：754 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 36.5k | — | 100 | 96.93 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 11.4k | — | 100 | 83.41 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 11.2k | — | 65 | 76.34 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：794 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：151 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | 193.6k | — | 100 | 100.00 | 终端 Agent 架构参考 |
| 2 | [Codex](https://github.com/openai/codex) | 104.1k | — | 100 | 100.00 | 完整 Coding Agent Harness 源码样本 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 83.2k | — | 100 | 99.44 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 79.3k | — | 100 | 99.30 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 225.8k | — | 100 | 90.00 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

首期仅建立基线；下一次刷新后生成真实增长榜。

#### 新发现观察池

- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)：67269 Stars；匹配度 3；omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- [xai-org/grok-build](https://github.com/xai-org/grok-build)：24175 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：237862 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：73292 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：46334 Stars；匹配度 2；Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
