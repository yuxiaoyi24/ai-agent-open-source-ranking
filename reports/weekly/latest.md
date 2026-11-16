# AI Agent 开源项目周榜（2026-11-16）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-11-09，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 45.0k | +335 | 100 | 86.21 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 30.7k | +135 | 100 | 82.61 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 14.7k | +102 | 100 | 80.79 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 22.2k | +79 | 100 | 80.43 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 61.0k | +299 | 100 | 78.65 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +335.0 | +0.75% | 75.28 |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | +299.0 | +0.49% | 70.71 |
| 3 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +135.0 | +0.44% | 69.75 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +102.0 | +0.70% | 68.22 |
| 5 | [Strands Harness SDK](https://github.com/strands-agents/harness-sdk) | +138.0 | +1.52% | 67.22 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1889 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：883 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：7059 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：5003 Stars；匹配度 2；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [openBitFun/OpenBitFun](https://github.com/openBitFun/OpenBitFun)：4032 Stars；匹配度 2；OpenBitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 24.4k | +151 | 100 | 82.72 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.7k | +24 | 100 | 67.02 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.7k | +13 | 100 | 63.83 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +151.0 | +0.62% | 70.47 |
| 2 | [Restate](https://github.com/restatedev/restate) | +24.0 | +0.51% | 55.93 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +13.0 | +0.78% | 52.63 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1282 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：8295 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：153 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenViking](https://github.com/volcengine/OpenViking) | 42.3k | +456 | 100 | 87.33 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 2 | [context-mode](https://github.com/mksglu/context-mode) | 34.2k | +441 | 100 | 87.08 | 独立 Context Manager 的直接样本 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 50.1k | +107 | 40 | 73.57 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 36.5k | +52 | 100 | 72.39 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.9k | +21 | 100 | 58.54 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | +441.0 | +1.31% | 77.55 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | +456.0 | +1.09% | 77.46 |
| 3 | [Continue](https://github.com/continuedev/continue) | +52.0 | +0.14% | 60.78 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +107.0 | +0.21% | 59.55 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +21.0 | +0.72% | 51.54 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：117461 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：80114 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [upstash/context7](https://github.com/upstash/context7)：64892 Stars；匹配度 2；Context7 Platform -- Up-to-date docs for AI agents
- [PostHog/posthog](https://github.com/PostHog/posthog)：40814 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：29212 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 69.0k | +367 | 100 | 87.00 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 33.3k | +186 | 100 | 83.80 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 25.5k | +66 | 85 | 77.81 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 12.4k | +83 | 100 | 72.38 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 30.4k | +176 | 100 | 68.50 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +367.0 | +0.53% | 75.68 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +186.0 | +0.56% | 71.67 |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | +176.0 | +0.58% | 63.86 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +66.0 | +0.26% | 63.39 |
| 5 | [MemOS](https://github.com/MemTensor/MemOS) | +83.0 | +0.67% | 63.23 |

#### 新发现观察池

- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：4321 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [oceanbase/powercontext](https://github.com/oceanbase/powercontext)：1685 Stars；匹配度 3；Agent memory: long-term memory & agent memory handoff. Claude Code & Codex.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1310 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1143 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：61272 Stars；匹配度 2；Hindsight: Agent Memory That Learns

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 94.2k | +418 | 100 | 80.32 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 40.7k | +99 | 100 | 74.52 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.9k | +66 | 100 | 73.69 | 文档和数据 Agent 基础栈 |
| 4 | [Haystack](https://github.com/deepset-ai/haystack) | 27.0k | +69 | 100 | 72.78 | 显式可控的 Context/RAG Pipeline |
| 5 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.7k | +51 | 100 | 72.34 | 图谱社区摘要与检索 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +418.0 | +0.45% | 72.68 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +99.0 | +0.24% | 64.29 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +66.0 | +0.12% | 62.25 |
| 4 | [Haystack](https://github.com/deepset-ai/haystack) | +69.0 | +0.26% | 62.15 |
| 5 | [GraphRAG](https://github.com/microsoft/graphrag) | +51.0 | +0.14% | 60.68 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38718 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：37513 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：144805 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：81838 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：80114 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Anthropic Skills](https://github.com/anthropics/skills) | 195.5k | +5583 | 100 | 92.94 | 官方 Skill 样本库 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | 318.2k | +3467 | 100 | 91.10 | Skill 驱动的软件工程方法 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 118.1k | +3798 | 100 | 85.82 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 27.3k | +245 | 100 | 84.59 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 325.4k | +6536 | 100 | 77.05 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Anthropic Skills](https://github.com/anthropics/skills) | +5583.0 | +2.94% | 85.88 |
| 2 | [agent-skills](https://github.com/addyosmani/agent-skills) | +3798.0 | +3.32% | 82.90 |
| 3 | [Superpowers](https://github.com/obra/superpowers) | +3467.0 | +1.10% | 82.20 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +6536.0 | +2.05% | 76.60 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +245.0 | +0.90% | 73.58 |

#### 新发现观察池

- [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage)：80798 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [wshobson/agents](https://github.com/wshobson/agents)：42561 Stars；匹配度 3；Plugins, agents, skills, and commands for Claude Code, Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi, written once in Markdown and adapted to each tool by generators with validation and evals.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：144805 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)：116407 Stars；匹配度 2；Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages
- [tt-a1i/archify](https://github.com/tt-a1i/archify)：96934 Stars；匹配度 2；Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.9k | +66 | 100 | 80.02 | Python 官方 SDK |
| 2 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.7k | +46 | 100 | 77.57 | MCP 规范与文档主仓库 |
| 3 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.8k | +55 | 100 | 77.54 | 企业工具网关和统一治理 |
| 4 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.8k | +38 | 100 | 77.44 | TypeScript 官方 SDK |
| 5 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 92.0k | +153 | 100 | 77.11 | 生态入口不代表每个 Server 均成熟 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +153.0 | +0.17% | 67.03 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +66.0 | +0.27% | 65.63 |
| 3 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | +55.0 | +1.15% | 65.07 |
| 4 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +46.0 | +0.48% | 63.43 |
| 5 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +38.0 | +0.28% | 62.39 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：97747 Stars；匹配度 2；A collection of MCP servers.
- [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute)：87874 Stars；匹配度 2；Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：79772 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57640 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：39704 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 18.2k | +1098 | 100 | 93.47 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 26.6k | +94 | 100 | 81.24 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 3.1k | +40 | 100 | 68.53 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +1098.0 | +6.43% | 91.38 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +94.0 | +0.36% | 67.63 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +40.0 | +1.31% | 59.66 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：551 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [BrightbeamAI/chap](https://github.com/BrightbeamAI/chap)：123 Stars；匹配度 3；CHAP, the Collaborative Human Agent Protocol, is a MCP/A2A-compatible runtime for auditable human-agent work: approvals, overrides, handoffs, escalation and verifiable evidence logs.
- [openJiuwen-ai/agent-protocol](https://github.com/openJiuwen-ai/agent-protocol)：116 Stars；匹配度 3；openJiuwen agent-protocol provides implementations of agent communication protocols, including C++ SDKs for MCP and A2A protocols.
- [auto-agent-protocol/auto-agent-protocol](https://github.com/auto-agent-protocol/auto-agent-protocol)：112 Stars；匹配度 3；The open automotive contract for MCP, A2A and Personal Agent Protocol: dealer discovery, inventory, evidence, pricing and consented inquiries.
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1460 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 36.1k | +418 | 100 | 79.38 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 18.0k | +15 | 100 | 67.64 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71.3k | +64 | 20 | 54.59 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +418.0 | +1.17% | 73.30 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +15.0 | +0.08% | 53.98 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +64.0 | +0.09% | 46.54 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：22143 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：122767 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：81838 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47948 Stars；匹配度 1；Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.
- [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)：47169 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 17.3k | +624 | 100 | 89.33 | Agent 原生 Sandbox Runtime |
| 2 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 7.1k | +2292 | 100 | 87.92 | 无完整容器的 OS 级限制 |
| 3 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 21.7k | +363 | 100 | 86.12 | NVIDIA 自主 Agent 安全 Runtime |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | 14.9k | +111 | 100 | 81.10 | 企业 Agent 云端安全执行环境 |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 13.3k | +65 | 100 | 71.61 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +2292.0 | +47.25% | 93.96 |
| 2 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +624.0 | +3.73% | 83.56 |
| 3 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +363.0 | +1.70% | 76.96 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +111.0 | +0.75% | 68.76 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +70.0 | +1.54% | 63.25 |

#### 新发现观察池

- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：5003 Stars；匹配度 3；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [deeplethe/sandstorm](https://github.com/deeplethe/sandstorm)：6099 Stars；匹配度 2；Run thousands of AI agent sandboxes on the cheapest machines.
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2435 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1919 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [Augani/dory](https://github.com/Augani/dory)：1637 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 121.2k | +770 | 100 | 89.89 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 32.4k | +378 | 100 | 86.41 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 26.1k | +81 | 100 | 80.73 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 8.0k | +34 | 100 | 68.83 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +4 | 100 | 60.07 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | +770.0 | +0.64% | 79.96 |
| 2 | [CUA](https://github.com/trycua/cua) | +378.0 | +1.18% | 76.47 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +81.0 | +0.31% | 66.78 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +34.0 | +0.43% | 57.92 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +4.0 | +0.28% | 46.28 |

#### 新发现观察池

- [Agenta-AI/awesome-ai-agent-platforms](https://github.com/Agenta-AI/awesome-ai-agent-platforms)：509 Stars；匹配度 3；A curated list of open-source AI agent platforms: AI coworkers and teammates, agent builders and frameworks, workflow automation platforms, browser agents, and coding agents, with licenses.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4138 Stars；匹配度 2；Open-source, vision-first browser agent
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1715 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1006 Stars；匹配度 2；Build browser agents for real world tasks
- [LvcidPsyche/auto-browser](https://github.com/LvcidPsyche/auto-browser)：929 Stars；匹配度 2；Give your AI agent a real browser — with a human in the loop. Open-source MCP-native browser agent.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 63.3k | +384 | 100 | 87.05 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 87.9k | +48073 | 100 | 84.78 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.4k | +37 | 40 | 60.82 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.1k | +6 | 85 | 53.88 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +48073.0 | +120.78% | 92.39 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +384.0 | +0.61% | 75.99 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +37.0 | +0.28% | 49.49 |
| 4 | [Plano](https://github.com/katanemo/plano) | +6.0 | +0.08% | 42.98 |

#### 新发现观察池

- [QuantumNous/new-api](https://github.com/QuantumNous/new-api)：51995 Stars；匹配度 4；Open-source AI gateway. Self-hosted LLM gateway with OpenAI-, Claude- and Gemini-compatible APIs, model routing, access control, usage tracking and cost accounting.
- [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute)：87874 Stars；匹配度 3；Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors
- [maximhq/bifrost](https://github.com/maximhq/bifrost)：9577 Stars；匹配度 3；Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-compatible API for 10,000+ models, with failover, load balancing, semantic caching, virtual keys, budgets and MCP Code Mode. Works with any SDK or agent and adds under 200µs of overhead at 5k RPS.
- [TykTechnologies/tyk](https://github.com/TykTechnologies/tyk)：10887 Stars；匹配度 2；Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol)
- [looplj/axonhub](https://github.com/looplj/axonhub)：5464 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 37.5k | +300 | 100 | 85.63 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 12.3k | +101 | 100 | 80.58 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 23.4k | +165 | 100 | 75.49 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 3.1k | +113 | 100 | 73.97 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.5k | +10 | 100 | 65.08 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +300.0 | +0.81% | 74.68 |
| 2 | [OpenLIT](https://github.com/openlit/openlit) | +113.0 | +3.80% | 69.83 |
| 3 | [Phoenix](https://github.com/Arize-ai/phoenix) | +101.0 | +0.83% | 68.27 |
| 4 | [Opik](https://github.com/comet-ml/opik) | +165.0 | +0.71% | 67.31 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +10.0 | +0.13% | 51.42 |

#### 新发现观察池

- [langwatch/langwatch](https://github.com/langwatch/langwatch)：5038 Stars；匹配度 3；Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company.
- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1570 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [Arize-ai/openinference](https://github.com/Arize-ai/openinference)：1322 Stars；匹配度 3；OpenTelemetry Instrumentation for Agent Observability
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：134 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：183 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 27.3k | +292 | 100 | 85.27 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 19.5k | +125 | 100 | 81.81 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 3.3k | +56 | 100 | 70.01 | 可复现评测任务框架 |
| 4 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 6.0k | +8 | 100 | 64.10 | Agent Evaluation 与 Testing |
| 5 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 6.2k | +36 | 65 | 63.46 | 真实代码 Issue 基准 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +292.0 | +1.08% | 74.82 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +125.0 | +0.65% | 69.37 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +56.0 | +1.75% | 62.26 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +36.0 | +0.58% | 53.05 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +8.0 | +0.13% | 50.20 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：378 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：1991 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：449 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：334 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：299 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 26.3k | +1330 | 100 | 93.01 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.9k | +96 | 100 | 80.01 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.5k | +50 | 100 | 70.06 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 477 | +1 | 20 | 35.93 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +1330.0 | +5.33% | 89.50 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +96.0 | +2.01% | 69.58 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +50.0 | +0.67% | 60.26 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +1.0 | +0.21% | 24.79 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：2046 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：595 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)：431 Stars；匹配度 3；Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents. Executable, testable rules for prompt injection, tool poisoning, context exfiltration and MCP attacks. Merged into open-source projects at Microsoft, Cisco, Gen Digital, MISP and FINOS. MIT-licensed.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：356 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：204 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.9k | +62 | 100 | 79.11 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 6.1k | +29 | 100 | 75.48 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.9k | +82 | 100 | 72.54 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Logto](https://github.com/logto-io/logto) | +62.0 | +0.42% | 65.17 |
| 2 | [Casdoor](https://github.com/casdoor/casdoor) | +82.0 | +0.55% | 63.09 |
| 3 | [OpenFGA](https://github.com/openfga/openfga) | +29.0 | +0.47% | 60.76 |

#### 新发现观察池

- [zalando-incubator/agentic-identity-broker](https://github.com/zalando-incubator/agentic-identity-broker)：80 Stars；匹配度 3；Identity broker for AI agents with OAuth2 delegation and consent management
- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：67 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8404 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2671 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：758 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38.7k | +150 | 100 | 83.27 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 13.2k | +230 | 100 | 76.51 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 12.9k | +44 | 100 | 70.30 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +230.0 | +1.77% | 70.60 |
| 2 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +150.0 | +0.39% | 70.38 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +44.0 | +0.34% | 59.44 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：795 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 135.5k | +1436 | 100 | 91.07 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | 227.1k | +1537 | 100 | 90.68 | 终端 Agent 架构参考 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 93.6k | +557 | 100 | 88.79 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 85.4k | +221 | 100 | 85.63 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 263.7k | +1869 | 100 | 83.21 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Codex](https://github.com/openai/codex) | +1436.0 | +1.07% | 82.14 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | +1537.0 | +0.68% | 81.36 |
| 3 | [herdr](https://github.com/herdrdev/herdr) | +1721.0 | +3.47% | 78.87 |
| 4 | [OpenHands](https://github.com/OpenHands/OpenHands) | +557.0 | +0.60% | 78.18 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +1869.0 | +0.71% | 77.68 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：27784 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [1jehuang/jcode](https://github.com/1jehuang/jcode)：21807 Stars；匹配度 3；High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：304002 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：81839 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：80462 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
