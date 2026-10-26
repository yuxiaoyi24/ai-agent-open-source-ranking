# AI Agent 开源项目周榜（2026-10-26）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-10-19，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 43.9k | +422 | 100 | 87.05 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 30.3k | +161 | 100 | 83.19 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Google ADK Python](https://github.com/google/adk-python) | 22.0k | +101 | 100 | 81.22 | 企业 Agent 生命周期覆盖完整 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 14.3k | +115 | 100 | 81.20 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 60.1k | +256 | 100 | 78.11 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +422.0 | +0.97% | 76.87 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +161.0 | +0.53% | 70.81 |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | +256.0 | +0.43% | 69.78 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +115.0 | +0.81% | 69.02 |
| 5 | [Google ADK Python](https://github.com/google/adk-python) | +101.0 | +0.46% | 68.04 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1888 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：877 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：7024 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4676 Stars；匹配度 2；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere)：3823 Stars；匹配度 2；Portable AI agent runtime for the JVM. One @Agent class runs on Spring AI, LangChain4j, Anthropic, or 9 more behind one SPI. Token streaming, tool calls, human approvals, and governance over WebSocket, SSE, gRPC, or WebTransport/HTTP3. Speaks MCP, A2A, and AG-UI.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 24.0k | +171 | 100 | 83.14 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.6k | +35 | 100 | 68.30 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.6k | +10 | 100 | 62.92 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +171.0 | +0.72% | 71.28 |
| 2 | [Restate](https://github.com/restatedev/restate) | +35.0 | +0.77% | 58.26 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +10.0 | +0.61% | 51.06 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1254 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：8182 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：141 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.
- [kkjiangk/agent-py](https://github.com/kkjiangk/agent-py)：101 Stars；匹配度 2；Personal AIOps engineering project with durable workflows, scoped hybrid retrieval, reliable event delivery, and verified API/browser contracts.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | 32.3k | +1463 | 100 | 92.78 | 独立 Context Manager 的直接样本 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | 40.8k | +545 | 100 | 88.04 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 49.8k | +124 | 40 | 74.02 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 36.3k | +69 | 100 | 73.23 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.8k | +18 | 100 | 57.97 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | +1463.0 | +4.75% | 88.51 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | +545.0 | +1.35% | 78.86 |
| 3 | [Continue](https://github.com/continuedev/continue) | +69.0 | +0.19% | 62.28 |
| 4 | [Aider](https://github.com/Aider-AI/aider) | +124.0 | +0.25% | 60.36 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +18.0 | +0.64% | 50.60 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：103172 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79529 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [upstash/context7](https://github.com/upstash/context7)：63689 Stars；匹配度 2；Context7 Platform -- Up-to-date docs for AI agents
- [PostHog/posthog](https://github.com/PostHog/posthog)：40441 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：28882 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 67.8k | +404 | 100 | 87.31 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 32.8k | +247 | 100 | 84.78 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 25.3k | +70 | 100 | 80.23 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 12.1k | +169 | 100 | 75.12 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 29.9k | +232 | 100 | 69.47 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +404.0 | +0.60% | 76.28 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +247.0 | +0.76% | 73.49 |
| 3 | [MemOS](https://github.com/MemTensor/MemOS) | +169.0 | +1.42% | 68.27 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +70.0 | +0.28% | 65.96 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | +232.0 | +0.78% | 65.63 |

#### 新发现观察池

- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：4731 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1289 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1123 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：53832 Stars；匹配度 2；Hindsight: Agent Memory That Learns
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)：29936 Stars；匹配度 2；TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 92.9k | +423 | 100 | 80.34 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 40.3k | +126 | 100 | 75.26 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.7k | +106 | 100 | 75.12 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.4k | +67 | 100 | 73.15 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.8k | +71 | 100 | 72.86 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +423.0 | +0.46% | 72.75 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +126.0 | +0.31% | 65.63 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +106.0 | +0.20% | 64.77 |
| 4 | [Haystack](https://github.com/deepset-ai/haystack) | +71.0 | +0.27% | 62.31 |
| 5 | [GraphRAG](https://github.com/microsoft/graphrag) | +67.0 | +0.18% | 62.12 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38705 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：35447 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：143070 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79529 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：79326 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Superpowers](https://github.com/obra/superpowers) | 305.2k | +3437 | 100 | 91.14 | Skill 驱动的软件工程方法 |
| 2 | [Anthropic Skills](https://github.com/anthropics/skills) | 183.8k | +1768 | 85 | 88.72 | 官方 Skill 样本库 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | 110.6k | +2278 | 100 | 84.60 | 生产级编码 Skill 样本 |
| 4 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 26.6k | +350 | 65 | 80.75 | Skill 可移植规范 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 303.4k | +6942 | 100 | 77.34 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Superpowers](https://github.com/obra/superpowers) | +3437.0 | +1.14% | 82.28 |
| 2 | [agent-skills](https://github.com/addyosmani/agent-skills) | +2278.0 | +2.10% | 80.46 |
| 3 | [Anthropic Skills](https://github.com/anthropics/skills) | +1768.0 | +0.97% | 79.69 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +6942.0 | +2.34% | 77.18 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +350.0 | +1.33% | 70.96 |

#### 新发现观察池

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)：71945 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：36584 Stars；匹配度 3；The open agent skills tool - npx skills
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：143070 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)：102587 Stars；匹配度 2；Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages
- [tt-a1i/archify](https://github.com/tt-a1i/archify)：89323 Stars；匹配度 2；Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.7k | +53 | 100 | 79.33 | Python 官方 SDK |
| 2 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.5k | +54 | 100 | 78.09 | MCP 规范与文档主仓库 |
| 3 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 91.6k | +204 | 100 | 77.98 | 生态入口不代表每个 Server 均成熟 |
| 4 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.7k | +42 | 100 | 77.74 | TypeScript 官方 SDK |
| 5 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.7k | +42 | 100 | 76.48 | 企业工具网关和统一治理 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +204.0 | +0.22% | 68.59 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +53.0 | +0.22% | 64.43 |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +54.0 | +0.57% | 64.40 |
| 4 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | +42.0 | +0.90% | 63.21 |
| 5 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +42.0 | +0.31% | 62.94 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：96873 Stars；匹配度 2；A collection of MCP servers.
- [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute)：81204 Stars；匹配度 2；Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：77836 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57614 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：38636 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 16.8k | +142 | 100 | 82.12 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 26.3k | +96 | 100 | 81.29 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 3.0k | +33 | 100 | 67.73 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +142.0 | +0.85% | 70.30 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +96.0 | +0.37% | 67.75 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +33.0 | +1.11% | 58.29 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：552 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [BrightbeamAI/chap](https://github.com/BrightbeamAI/chap)：121 Stars；匹配度 3；CHAP, the Collaborative Human Agent Protocol, is a MCP/A2A-compatible runtime for auditable human-agent work: approvals, overrides, handoffs, escalation and verifiable evidence logs.
- [openJiuwen-ai/agent-protocol](https://github.com/openJiuwen-ai/agent-protocol)：115 Stars；匹配度 3；openJiuwen agent-protocol provides implementations of agent communication protocols, including C++ SDKs for MCP and A2A protocols.
- [auto-agent-protocol/auto-agent-protocol](https://github.com/auto-agent-protocol/auto-agent-protocol)：110 Stars；匹配度 3；The open automotive contract for MCP, A2A and Personal Agent Protocol: dealer discovery, inventory, evidence, pricing and consented inquiries.
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1460 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 34.1k | +579 | 100 | 80.78 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 18.0k | +41 | 100 | 70.57 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71.0k | +103 | 20 | 56.00 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +579.0 | +1.73% | 76.01 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +41.0 | +0.23% | 59.15 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +103.0 | +0.15% | 49.03 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：22080 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：114871 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：79326 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)：49353 Stars；匹配度 1；Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47588 Stars；匹配度 1；Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 19.9k | +3282 | 100 | 97.20 | NVIDIA 自主 Agent 安全 Runtime |
| 2 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 6.6k | +1781 | 100 | 87.79 | 无完整容器的 OS 级限制 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 16.2k | +212 | 100 | 83.69 | Agent 原生 Sandbox Runtime |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | 14.6k | +121 | 100 | 81.40 | 企业 Agent 云端安全执行环境 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 4.4k | +83 | 100 | 71.83 | K8s 上 Agent 隔离工作负载 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +3282.0 | +19.72% | 98.60 |
| 2 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +1781.0 | +36.71% | 93.89 |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +212.0 | +1.33% | 73.24 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +121.0 | +0.84% | 69.34 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +83.0 | +1.93% | 64.84 |

#### 新发现观察池

- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4676 Stars；匹配度 3；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2330 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1686 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [Augani/dory](https://github.com/Augani/dory)：1634 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.
- [cloudflare/artifact-fs](https://github.com/cloudflare/artifact-fs)：1203 Stars；匹配度 2；ArtifactFS is a filesystem driver designed to mount large git repos as quickly as possible, hydrating file contents on-the-fly instead of blocking on the initial clone. It's ideal for agents, sandboxes, containers and other use-cases where startup time is critical.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CUA](https://github.com/trycua/cua) | 31.0k | +808 | 100 | 90.03 | Computer Use 驱动和训练评测平台 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | 119.1k | +695 | 100 | 89.54 | 浏览器 Agent 主流实现 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 25.8k | +80 | 100 | 80.68 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.9k | +32 | 100 | 68.62 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +8 | 100 | 62.04 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CUA](https://github.com/trycua/cua) | +808.0 | +2.68% | 83.26 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | +695.0 | +0.59% | 79.34 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +80.0 | +0.31% | 66.71 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +32.0 | +0.41% | 57.57 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +8.0 | +0.57% | 49.82 |

#### 新发现观察池

- [Agenta-AI/awesome-ai-agent-platforms](https://github.com/Agenta-AI/awesome-ai-agent-platforms)：669 Stars；匹配度 3；A curated list of open-source AI agent platforms: AI coworkers and teammates, agent builders and frameworks, workflow automation platforms, browser agents, and coding agents, with licenses.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4136 Stars；匹配度 2；Open-source, vision-first browser agent
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1544 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1006 Stars；匹配度 2；Build browser agents for real world tasks
- [outcrawlai/scout](https://github.com/outcrawlai/scout)：939 Stars；匹配度 2；Scout: the open-source browser agent, by Outcrawl. Mirrored automatically from Outcrawl's own repository.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 62.0k | +514 | 100 | 88.08 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 81.2k | +2994 | 100 | 78.47 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.3k | +58 | 40 | 62.24 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.1k | +7 | 100 | 56.52 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2994.0 | +3.83% | 79.98 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +514.0 | +0.84% | 77.89 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +58.0 | +0.44% | 52.03 |
| 4 | [Plano](https://github.com/katanemo/plano) | +7.0 | +0.10% | 45.94 |

#### 新发现观察池

- [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute)：81204 Stars；匹配度 3；Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors
- [maximhq/bifrost](https://github.com/maximhq/bifrost)：9101 Stars；匹配度 3；Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-compatible API for 10,000+ models, with failover, load balancing, semantic caching, virtual keys, budgets and MCP Code Mode. Works with any SDK or agent and adds under 200µs of overhead at 5k RPS.
- [TykTechnologies/tyk](https://github.com/TykTechnologies/tyk)：10870 Stars；匹配度 2；Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol)
- [looplj/axonhub](https://github.com/looplj/axonhub)：5398 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
- [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models)：5227 Stars；匹配度 2；Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows.

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 36.5k | +479 | 100 | 87.45 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 12.0k | +100 | 100 | 80.52 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 22.9k | +198 | 100 | 76.14 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 2.9k | +25 | 100 | 66.65 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.5k | +6 | 100 | 63.72 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +479.0 | +1.33% | 78.07 |
| 2 | [Opik](https://github.com/comet-ml/opik) | +198.0 | +0.87% | 68.53 |
| 3 | [Phoenix](https://github.com/Arize-ai/phoenix) | +100.0 | +0.84% | 68.22 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +25.0 | +0.87% | 56.43 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +6.0 | +0.08% | 49.02 |

#### 新发现观察池

- [langwatch/langwatch](https://github.com/langwatch/langwatch)：4991 Stars；匹配度 3；Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company.
- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1554 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：127 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：186 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：148 Stars；匹配度 2；无仓库描述

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 26.4k | +304 | 100 | 85.41 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 19.1k | +162 | 100 | 82.73 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 3.1k | +54 | 100 | 69.84 | 可复现评测任务框架 |
| 4 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.9k | +13 | 100 | 65.45 | Agent Evaluation 与 Testing |
| 5 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 6.1k | +37 | 65 | 63.53 | 真实代码 Issue 基准 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +304.0 | +1.16% | 75.15 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +162.0 | +0.86% | 71.08 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +54.0 | +1.78% | 62.09 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +37.0 | +0.61% | 53.22 |
| 5 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | +13.0 | +0.22% | 52.61 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：375 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：598 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：448 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：332 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：208 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 21.6k | +1116 | 100 | 92.78 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.7k | +38 | 100 | 76.11 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.4k | +41 | 100 | 69.35 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 475 | +3 | 20 | 38.36 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +1116.0 | +5.44% | 89.55 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +38.0 | +0.82% | 62.54 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +41.0 | +0.56% | 59.04 |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | +3.0 | +0.64% | 29.15 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：2028 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：586 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)：422 Stars；匹配度 3；Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents. Executable, testable rules for prompt injection, tool poisoning, context exfiltration and MCP attacks. Merged into open-source projects at Microsoft, Cisco, Gen Digital, MISP and FINOS. MIT-licensed.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：344 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：203 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.8k | +101 | 100 | 80.76 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 6.0k | +38 | 100 | 76.36 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.7k | +63 | 100 | 71.64 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Logto](https://github.com/logto-io/logto) | +101.0 | +0.69% | 68.15 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | +38.0 | +0.63% | 62.39 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +63.0 | +0.43% | 61.52 |

#### 新发现观察池

- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：67 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8403 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2678 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [VibeTensor/attestix](https://github.com/VibeTensor/attestix)：837 Stars；匹配度 2；AI agent identity, signed credentials, delegated authority and portable governance evidence. Python core and offline verifier SDKs.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 12.5k | +815 | 100 | 85.27 | 复杂编码任务的人机协作样本 |
| 2 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38.2k | +136 | 100 | 82.93 | Agent 前端和 AG-UI 实现 |
| 3 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12.7k | +141 | 100 | 74.39 | React Agent UI 组件库 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +815.0 | +6.96% | 87.34 |
| 2 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +136.0 | +0.36% | 69.81 |
| 3 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +141.0 | +1.12% | 66.81 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：795 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | 221.6k | +4788 | 100 | 92.21 | 终端 Agent 架构参考 |
| 2 | [Codex](https://github.com/openai/codex) | 130.9k | +1110 | 100 | 90.86 | 完整 Coding Agent Harness 源码样本 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 91.9k | +629 | 100 | 89.20 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 84.4k | +331 | 100 | 86.91 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 257.1k | +2114 | 100 | 83.33 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) | +4788.0 | +2.21% | 84.42 |
| 2 | [Codex](https://github.com/openai/codex) | +1110.0 | +0.86% | 81.71 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | +629.0 | +0.69% | 78.96 |
| 4 | [Paperclip](https://github.com/paperclipai/paperclip) | +3123.0 | +3.00% | 78.49 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +2114.0 | +0.83% | 77.91 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：27545 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [1jehuang/jcode](https://github.com/1jehuang/jcode)：21210 Stars；匹配度 3；High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- [zai-org/ZCode](https://github.com/zai-org/ZCode)：8245 Stars；匹配度 3；Z.ai's coding agent harness. Powerful, intelligent, extensible.
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：288990 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：79326 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
