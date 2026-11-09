# AI Agent 开源项目周榜（2026-11-09）

> 自动生成；正式榜单来自人工策展候选池，搜索发现只进入观察池。

## 本期口径

- 对比快照：2026-11-02，Stars 增量已折算为 7 天口径。
- 综合榜：架构相关度、基础热度、周增量、活跃度和仓库健康度。
- 增长榜：周 Stars 增量/增速为主，保留架构相关度和活跃度约束。
- Stars 只代表社区信号，不代表生产成熟度或许可证可用性。

## 模块周榜

### Agent Runtime / SDK

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 44.7k | +371 | 100 | 86.57 | 有状态可恢复 Agent Runtime 的首选源码样本 |
| 2 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | 30.6k | +119 | 100 | 82.19 | 用最小抽象观察 Agent loop 和 handoff |
| 3 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 14.6k | +110 | 100 | 81.05 | Microsoft 新统一路线需与 AutoGen/SK 对照 |
| 4 | [Google ADK Python](https://github.com/google/adk-python) | 22.2k | +73 | 100 | 80.17 | 企业 Agent 生命周期覆盖完整 |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 60.7k | +273 | 100 | 78.34 | 角色协作和 Flow 双层抽象 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | +371.0 | +0.84% | 75.96 |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | +273.0 | +0.45% | 70.16 |
| 3 | [OpenAI Agents SDK Python](https://github.com/openai/openai-agents-python) | +119.0 | +0.39% | 69.01 |
| 4 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | +110.0 | +0.76% | 68.71 |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | +157.0 | +0.54% | 66.91 |

#### 新发现观察池

- [Yuan-lab-LLM/ClawManager](https://github.com/Yuan-lab-LLM/ClawManager)：1888 Stars；匹配度 3；A Kubernetes-native control plane for AI agent instance management, with governed AI access, runtime orchestration, and reusable resources across multiple agent runtimes.
- [agentscope-ai/agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)：880 Stars；匹配度 3；A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)：7052 Stars；匹配度 2；Self-hosted TypeScript agent runtime with durable approvals and verifiable run records. Own it, approve it, audit it.
- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4896 Stars；匹配度 2；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [GCWing/OpenBitFun](https://github.com/GCWing/OpenBitFun)：3983 Stars；匹配度 2；OpenBitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent with open, general-purpose capabilities for work beyond software development.

### Durable Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Temporal](https://github.com/temporalio/temporal) | 24.3k | +145 | 100 | 82.57 | 验证状态恢复与业务副作用一致性 |
| 2 | [Restate](https://github.com/restatedev/restate) | 4.7k | +36 | 100 | 68.41 | 轻量 durable execution 路线 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | 1.7k | +10 | 100 | 62.94 | 数据库支撑的 Python 持久化工作流 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Temporal](https://github.com/temporalio/temporal) | +145.0 | +0.60% | 70.22 |
| 2 | [Restate](https://github.com/restatedev/restate) | +36.0 | +0.78% | 58.44 |
| 3 | [DBOS Transact Python](https://github.com/dbos-inc/dbos-transact-py) | +10.0 | +0.60% | 51.05 |

#### 新发现观察池

- [durable-workflow/workflow](https://github.com/durable-workflow/workflow)：1279 Stars；匹配度 3；Core package for defining and running durable workflows and activities. Supports long-running persistent workflows, retries, queues, parallel execution, workflow monitoring, dedicated storage connections, and orchestration for microservices, data pipelines, sagas, agentic workflows, and other complex business processes.
- [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)：8251 Stars；匹配度 2；🪓 An orchestration engine for background tasks, AI agents, and durable workflows
- [jcarlosrodicio/opencode-agent-orchestration-kit](https://github.com/jcarlosrodicio/opencode-agent-orchestration-kit)：150 Stars；匹配度 2；Open-source multi-agent orchestration harness for OpenCode — specialized agents, durable workflows, research, planning, implementation, review, and validation.
- [kkjiangk/agent-py](https://github.com/kkjiangk/agent-py)：101 Stars；匹配度 2；Personal AIOps engineering project with durable workflows, scoped hybrid retrieval, reliable event delivery, and verified API/browser contracts.

### Context Manager

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | 33.7k | +526 | 100 | 87.84 | 独立 Context Manager 的直接样本 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | 41.8k | +502 | 100 | 87.71 | 统一 Memory/Knowledge/Skills 的 Context Database |
| 3 | [Aider](https://github.com/Aider-AI/aider) | 50.0k | +139 | 40 | 74.38 | 代码图和 token 预算的成熟实现 |
| 4 | [Continue](https://github.com/continuedev/continue) | 36.4k | +40 | 100 | 71.61 | IDE 场景上下文装配 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | 2.9k | +37 | 100 | 60.67 | 本体和 Context Graph 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [context-mode](https://github.com/mksglu/context-mode) | +526.0 | +1.58% | 78.98 |
| 2 | [OpenViking](https://github.com/volcengine/OpenViking) | +502.0 | +1.21% | 78.19 |
| 3 | [Aider](https://github.com/Aider-AI/aider) | +139.0 | +0.28% | 60.99 |
| 4 | [Continue](https://github.com/continuedev/continue) | +40.0 | +0.11% | 59.41 |
| 5 | [TrustGraph](https://github.com/trustgraph-ai/trustgraph) | +37.0 | +1.29% | 55.44 |

#### 新发现观察池

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)：115050 Stars；匹配度 2；Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79930 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [upstash/context7](https://github.com/upstash/context7)：64393 Stars；匹配度 2；Context7 Platform -- Up-to-date docs for AI agents
- [PostHog/posthog](https://github.com/PostHog/posthog)：40708 Stars；匹配度 2；:hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)：29136 Stars；匹配度 2；A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

### Agent Memory

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | 68.7k | +407 | 100 | 87.35 | 通用 Agent Memory Layer |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | 33.2k | +162 | 100 | 83.32 | 知识图谱驱动长期记忆 |
| 3 | [Letta](https://github.com/letta-ai/letta) | 25.4k | +71 | 85 | 78.03 | 上下文自编辑与有状态 Agent |
| 4 | [MemOS](https://github.com/MemTensor/MemOS) | 12.3k | +106 | 100 | 73.26 | 自演进 Memory OS 路线 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | 30.2k | +139 | 100 | 67.69 | 增长快且 benchmark 声明需复现 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Mem0](https://github.com/mem0ai/mem0) | +407.0 | +0.60% | 76.32 |
| 2 | [Cognee](https://github.com/topoteretes/cognee) | +162.0 | +0.49% | 70.83 |
| 3 | [MemOS](https://github.com/MemTensor/MemOS) | +106.0 | +0.87% | 64.84 |
| 4 | [Letta](https://github.com/letta-ai/letta) | +71.0 | +0.28% | 63.79 |
| 5 | [agentmemory](https://github.com/rohitg00/agentmemory) | +139.0 | +0.46% | 62.42 |

#### 新发现观察池

- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)：4314 Stars；匹配度 3；Long-term memory runtime for AI agents — plain Markdown as the source of truth, local ranked retrieval, and an independent sleep-time Manage layer. Claude Code and Codex share one store. No API key.
- [oceanbase/powercontext](https://github.com/oceanbase/powercontext)：1543 Stars；匹配度 3；Agent memory: long-term memory & agent memory handoff. Claude Code & Codex.
- [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)：1300 Stars；匹配度 3；Awesome AI Memory | LLM Memory | A curated knowledge base on AI memory for LLMs and agents, covering long-term memory, reasoning, retrieval, and memory-native system design.  Awesome-AI-Memory 是一个 集中式、持续更新的 AI 记忆知识库，系统性整理了与 大模型记忆（LLM Memory）与智能体记忆（Agent Memory） 相关的前沿研究、工程框架、系统设计、评测基准与真实应用实践。
- [NirDiamant/Agent_Memory_Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)：1137 Stars；匹配度 3；Agent memory for LLMs: 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks, and production patterns.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)：59967 Stars；匹配度 2；Hindsight: Agent Memory That Learns

### Knowledge / RAG

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | 93.8k | +481 | 100 | 80.79 | 完整 RAG 工程链和 Context Layer |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | 40.6k | +141 | 100 | 75.63 | 轻量图 RAG 和增量更新 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | 52.9k | +74 | 100 | 74.03 | 文档和数据 Agent 基础栈 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | 36.6k | +73 | 100 | 73.42 | 图谱社区摘要与检索 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 26.9k | +39 | 100 | 71.05 | 显式可控的 Context/RAG Pipeline |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [RAGFlow](https://github.com/infiniflow/ragflow) | +481.0 | +0.52% | 73.53 |
| 2 | [LightRAG](https://github.com/HKUDS/LightRAG) | +141.0 | +0.35% | 66.27 |
| 3 | [LlamaIndex](https://github.com/run-llama/llama_index) | +74.0 | +0.14% | 62.85 |
| 4 | [GraphRAG](https://github.com/microsoft/graphrag) | +73.0 | +0.20% | 62.58 |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | +39.0 | +0.14% | 59.09 |

#### 新发现观察池

- [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)：38712 Stars；匹配度 3；Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM, Qwen 与 Llama 等语言模型的 RAG 与 Agent 应用 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM, Qwen and Llama) RAG and Agent app with langchain
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora)：36917 Stars；匹配度 3；Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：144239 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：81304 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)：79930 Stars；匹配度 2；🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

### Agent Skills

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Anthropic Skills](https://github.com/anthropics/skills) | 189.9k | +3472 | 100 | 91.86 | 官方 Skill 样本库 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | 314.7k | +3933 | 100 | 91.27 | Skill 驱动的软件工程方法 |
| 3 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | 27.1k | +227 | 100 | 84.30 | Skill 可移植规范 |
| 4 | [agent-skills](https://github.com/addyosmani/agent-skills) | 114.3k | +1641 | 100 | 83.96 | 生产级编码 Skill 样本 |
| 5 | [mattpocock skills](https://github.com/mattpocock/skills) | 318.9k | +9428 | 100 | 78.05 | 高传播度内容样本不等于 Runtime |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Anthropic Skills](https://github.com/anthropics/skills) | +3472.0 | +1.86% | 83.72 |
| 2 | [Superpowers](https://github.com/obra/superpowers) | +3933.0 | +1.27% | 82.53 |
| 3 | [agent-skills](https://github.com/addyosmani/agent-skills) | +1641.0 | +1.46% | 79.16 |
| 4 | [mattpocock skills](https://github.com/mattpocock/skills) | +9428.0 | +3.05% | 78.59 |
| 5 | [Agent Skills Specification](https://github.com/agentskills/agentskills) | +227.0 | +0.85% | 73.07 |

#### 新发现观察池

- [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage)：78803 Stars；匹配度 3；World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
- [wshobson/agents](https://github.com/wshobson/agents)：42338 Stars；匹配度 3；Plugins, agents, skills, and commands for Claude Code, Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot, and Pi, written once in Markdown and adapted to each tool by generators with validation and evals.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)：144239 Stars；匹配度 2；100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)：112164 Stars；匹配度 2；Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages
- [tt-a1i/archify](https://github.com/tt-a1i/archify)：94841 Stars；匹配度 2；Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

### MCP / Tool Infrastructure

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 24.8k | +70 | 100 | 80.20 | Python 官方 SDK |
| 2 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 9.7k | +63 | 100 | 78.64 | MCP 规范与文档主仓库 |
| 3 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 13.7k | +40 | 100 | 77.60 | TypeScript 官方 SDK |
| 4 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | 91.9k | +132 | 100 | 76.66 | 生态入口不代表每个 Server 均成熟 |
| 5 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | 4.8k | +35 | 100 | 75.83 | 企业工具网关和统一治理 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [MCP Servers](https://github.com/modelcontextprotocol/servers) | +132.0 | +0.14% | 66.24 |
| 2 | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | +70.0 | +0.28% | 65.95 |
| 3 | [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | +63.0 | +0.66% | 65.36 |
| 4 | [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | +40.0 | +0.29% | 62.68 |
| 5 | [MCP Context Forge](https://github.com/IBM/mcp-context-forge) | +35.0 | +0.74% | 61.99 |

#### 新发现观察池

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：97503 Stars；匹配度 2；A collection of MCP servers.
- [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute)：85781 Stars；匹配度 2；Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)：79185 Stars；匹配度 2；Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)：57634 Stars；匹配度 2；Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)：39357 Stars；匹配度 2；Playwright MCP server

### Agent Interoperability Protocol

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | 17.1k | +104 | 100 | 81.02 | Agent 到 UI 的事件协议 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | 26.5k | +74 | 100 | 80.47 | Agent 到 Agent 的远程互操作 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | 3.1k | +27 | 100 | 66.98 | MCP Server 提供嵌入式 UI |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | +104.0 | +0.61% | 68.27 |
| 2 | [A2A](https://github.com/a2aproject/A2A) | +74.0 | +0.28% | 66.28 |
| 3 | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) | +27.0 | +0.89% | 56.88 |

#### 新发现观察池

- [win4r/openclaw-a2a-gateway](https://github.com/win4r/openclaw-a2a-gateway)：550 Stars；匹配度 3；OpenClaw plugin implementing the A2A (Agent-to-Agent) protocol v0.3.0 — bidirectional agent communication gateway
- [BrightbeamAI/chap](https://github.com/BrightbeamAI/chap)：122 Stars；匹配度 3；CHAP, the Collaborative Human Agent Protocol, is a MCP/A2A-compatible runtime for auditable human-agent work: approvals, overrides, handoffs, escalation and verifiable evidence logs.
- [openJiuwen-ai/agent-protocol](https://github.com/openJiuwen-ai/agent-protocol)：115 Stars；匹配度 3；openJiuwen agent-protocol provides implementations of agent communication protocols, including C++ SDKs for MCP and A2A protocols.
- [auto-agent-protocol/auto-agent-protocol](https://github.com/auto-agent-protocol/auto-agent-protocol)：111 Stars；匹配度 3；The open automotive contract for MCP, A2A and Personal Agent Protocol: dealer discovery, inventory, evidence, pricing and consented inquiries.
- [agi-inc/agent-protocol](https://github.com/agi-inc/agent-protocol)：1460 Stars；匹配度 2；Common interface for interacting with AI agents. The protocol is tech stack agnostic - you can use it with any framework for building agents.

### Multi-Agent Coordination

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | 35.7k | +481 | 100 | 79.96 | 国内多 Agent Runtime 代表 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | 18.0k | +13 | 100 | 67.24 | 多 Agent 社会与规模化研究 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71.2k | +92 | 20 | 55.66 | 以角色和中间产物模拟软件组织 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [AgentScope](https://github.com/agentscope-ai/agentscope) | +481.0 | +1.37% | 74.39 |
| 2 | [CAMEL](https://github.com/camel-ai/camel) | +13.0 | +0.07% | 53.28 |
| 3 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | +92.0 | +0.13% | 48.43 |

#### 新发现观察池

- [openai/swarm](https://github.com/openai/swarm)：22116 Stars；匹配度 2；Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)：121431 Stars；匹配度 1；TradingAgents: Multi-Agents LLM Financial Trading Framework
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：81304 Stars；匹配度 1；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)：47847 Stars；匹配度 1；Open-source personal AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install.
- [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)：46875 Stars；匹配度 1；Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### Sandbox / Code Execution

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | 7.0k | +2188 | 100 | 87.89 | 无完整容器的 OS 级限制 |
| 2 | [OpenShell](https://github.com/NVIDIA/OpenShell) | 21.3k | +366 | 100 | 86.16 | NVIDIA 自主 Agent 安全 Runtime |
| 3 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 16.7k | +338 | 100 | 85.82 | Agent 原生 Sandbox Runtime |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | 14.8k | +109 | 100 | 81.03 | 企业 Agent 云端安全执行环境 |
| 5 | [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | 13.2k | +71 | 100 | 71.91 | 国内高并发轻量 Sandbox 路线 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | +2188.0 | +45.10% | 93.95 |
| 2 | [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +338.0 | +2.06% | 77.09 |
| 3 | [OpenShell](https://github.com/NVIDIA/OpenShell) | +366.0 | +1.75% | 77.08 |
| 4 | [E2B](https://github.com/e2b-dev/E2B) | +109.0 | +0.74% | 68.64 |
| 5 | [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | +74.0 | +1.65% | 63.75 |

#### 新发现观察池

- [nolabs-ai/nono](https://github.com/nolabs-ai/nono)：4896 Stars；匹配度 3；agent runtime security - zero trust, zero setup, zero latency agent sandboxing
- [deeplethe/sandstorm](https://github.com/deeplethe/sandstorm)：5954 Stars；匹配度 2；Run thousands of AI agent sandboxes on the cheapest machines.
- [earendil-works/gondolin](https://github.com/earendil-works/gondolin)：2403 Stars；匹配度 2；Experimental Linux microvm setup with a TypeScript Control Plane as Agent Sandbox
- [BitMiracle-AI/Dormice](https://github.com/BitMiracle-AI/Dormice)：1841 Stars；匹配度 2；The SQLite of agent sandboxes — self-hosted, E2B-compatible. One machine, sandboxes that live forever, idle costs nothing.
- [Augani/dory](https://github.com/Augani/dory)：1637 Stars；匹配度 2；Dory is the complete local development system for Apple Silicon: Docker, Compose, Kubernetes, virtual machines, and policy-bound agent sandboxes.

### Browser / Computer Use

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Browser-use](https://github.com/browser-use/browser-use) | 120.4k | +590 | 100 | 88.97 | 浏览器 Agent 主流实现 |
| 2 | [CUA](https://github.com/trycua/cua) | 32.0k | +488 | 100 | 87.50 | Computer Use 驱动和训练评测平台 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | 26.0k | +85 | 100 | 80.88 | 确定性浏览器 API 与 Agent 结合 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | 7.9k | +36 | 100 | 69.01 | 开源 Browser API 和 Sandbox |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | 1.4k | +9 | 100 | 62.43 | 浏览器任务环境与评测 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CUA](https://github.com/trycua/cua) | +488.0 | +1.55% | 78.48 |
| 2 | [Browser-use](https://github.com/browser-use/browser-use) | +590.0 | +0.49% | 78.32 |
| 3 | [Stagehand](https://github.com/browserbase/stagehand) | +85.0 | +0.33% | 67.06 |
| 4 | [Steel Browser](https://github.com/steel-dev/steel-browser) | +36.0 | +0.46% | 58.26 |
| 5 | [BrowserGym](https://github.com/ServiceNow/BrowserGym) | +9.0 | +0.63% | 50.49 |

#### 新发现观察池

- [Agenta-AI/awesome-ai-agent-platforms](https://github.com/Agenta-AI/awesome-ai-agent-platforms)：504 Stars；匹配度 3；A curated list of open-source AI agent platforms: AI coworkers and teammates, agent builders and frameworks, workflow automation platforms, browser agents, and coding agents, with licenses.
- [magnitudedev/browser-agent](https://github.com/magnitudedev/browser-agent)：4139 Stars；匹配度 2；Open-source, vision-first browser agent
- [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain)：1682 Stars；匹配度 2；Open-source AI browser agent for Chrome and Firefox (monorepo) 🧠
- [Planetary-Computers/autotab-starter](https://github.com/Planetary-Computers/autotab-starter)：1007 Stars；匹配度 2；Build browser agents for real world tasks
- [LvcidPsyche/auto-browser](https://github.com/LvcidPsyche/auto-browser)：924 Stars；匹配度 2；Give your AI agent a real browser — with a human in the loop. Open-source MCP-native browser agent.

### Model Gateway / Routing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [LiteLLM](https://github.com/BerriAI/litellm) | 62.9k | +420 | 100 | 87.36 | 多模型统一入口与治理 |
| 2 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 85.8k | +45980 | 100 | 84.73 | 增长快且功能宽需持续复核 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | 13.3k | +48 | 40 | 61.63 | 高性能多模型网关 |
| 4 | [Plano](https://github.com/katanemo/plano) | 7.1k | +8 | 85 | 54.63 | Agentic App Data Plane |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +45980.0 | +115.52% | 92.37 |
| 2 | [LiteLLM](https://github.com/BerriAI/litellm) | +420.0 | +0.67% | 76.56 |
| 3 | [Portkey Gateway](https://github.com/Portkey-AI/gateway) | +48.0 | +0.36% | 50.94 |
| 4 | [Plano](https://github.com/katanemo/plano) | +8.0 | +0.11% | 44.31 |

#### 新发现观察池

- [QuantumNous/new-api](https://github.com/QuantumNous/new-api)：51584 Stars；匹配度 4；Open-source AI gateway. Self-hosted LLM gateway with OpenAI-, Claude- and Gemini-compatible APIs, model routing, access control, usage tracking and cost accounting.
- [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute)：85781 Stars；匹配度 3；Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 900+ contributors
- [maximhq/bifrost](https://github.com/maximhq/bifrost)：9444 Stars；匹配度 3；Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-compatible API for 10,000+ models, with failover, load balancing, semantic caching, virtual keys, budgets and MCP Code Mode. Works with any SDK or agent and adds under 200µs of overhead at 5k RPS.
- [TykTechnologies/tyk](https://github.com/TykTechnologies/tyk)：10879 Stars；匹配度 2；Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol)
- [looplj/axonhub](https://github.com/looplj/axonhub)：5441 Stars；匹配度 2；⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.

### Agent Observability

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | 37.2k | +316 | 100 | 85.81 | 自托管 AI Engineering 平台 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | 12.2k | +111 | 100 | 80.93 | OTel 路线的 Agent 可观测评测 |
| 3 | [Opik](https://github.com/comet-ml/opik) | 23.3k | +166 | 100 | 75.50 | 观测评测一体化 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | 3.0k | +70 | 100 | 71.15 | AI Engineering 多治理能力 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | 7.5k | +10 | 100 | 65.08 | LLM/Agent OTel instrumentation |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Langfuse](https://github.com/langfuse/langfuse) | +316.0 | +0.86% | 75.03 |
| 2 | [Phoenix](https://github.com/Arize-ai/phoenix) | +111.0 | +0.92% | 68.92 |
| 3 | [Opik](https://github.com/comet-ml/opik) | +166.0 | +0.72% | 67.35 |
| 4 | [OpenLIT](https://github.com/openlit/openlit) | +70.0 | +2.41% | 64.62 |
| 5 | [OpenLLMetry](https://github.com/traceloop/openllmetry) | +10.0 | +0.13% | 51.42 |

#### 新发现观察池

- [langwatch/langwatch](https://github.com/langwatch/langwatch)：5019 Stars；匹配度 3；Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding assistant in the company.
- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)：1566 Stars；匹配度 3；Real-time monitoring for Claude Code agents through simple hook event tracking.
- [traccia-ai/traccia-py](https://github.com/traccia-ai/traccia-py)：133 Stars；匹配度 3；OpenTelemetry-native SDK for AI agent observability, tracing, evaluation, debugging, governance, and runtime policy enforcement. Framework-agnostic and built for OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.
- [hoangperry/herminal](https://github.com/hoangperry/herminal)：183 Stars；匹配度 2；Local-first native macOS terminal with Vietnamese IME support and coding-agent observability
- [disler/pi-agent-observability](https://github.com/disler/pi-agent-observability)：148 Stars；匹配度 2；无仓库描述

### Agent Evaluation / Testing

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | 27.0k | +255 | 100 | 84.73 | 声明式评测与安全扫描 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | 19.4k | +140 | 100 | 82.21 | LLM/Agent Evaluation Framework |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | 3.2k | +54 | 100 | 69.84 | 可复现评测任务框架 |
| 4 | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) | 5.9k | +6 | 100 | 63.33 | Agent Evaluation 与 Testing |
| 5 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | 6.2k | +33 | 65 | 63.16 | 真实代码 Issue 基准 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Promptfoo](https://github.com/promptfoo/promptfoo) | +255.0 | +0.95% | 73.87 |
| 2 | [DeepEval](https://github.com/confident-ai/deepeval) | +140.0 | +0.73% | 70.10 |
| 3 | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | +54.0 | +1.71% | 61.99 |
| 4 | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | +33.0 | +0.54% | 52.52 |
| 5 | [OpenEvals](https://github.com/langchain-ai/openevals) | +9.0 | +0.73% | 50.56 |

#### 新发现观察池

- [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)：377 Stars；匹配度 4；A generative AI-powered framework for testing virtual agents.
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)：660 Stars；匹配度 3；Multi-tier framework for evaluating AI agent skills with quality gates, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior.
- [canwhite/AgentEval](https://github.com/canwhite/AgentEval)：449 Stars；匹配度 3；The agent responsible for conducting the agent evaluation
- [reworkd/bananalyzer](https://github.com/reworkd/bananalyzer)：332 Stars；匹配度 3；Open source AI Agent evaluation framework for web tasks 🐒🍌
- [P90-RushB/AgentArk](https://github.com/P90-RushB/AgentArk)：210 Stars；匹配度 3；A General-Purpose Environment Framework for Scalable Multimodal Agent Evaluation and RL

### Agent Security / Guardrails

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 25.0k | +1058 | 100 | 92.02 | Agent Skill 供应链安全 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | 4.8k | +49 | 100 | 77.08 | 生成式 AI 风险识别与自动红队 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 7.5k | +46 | 100 | 69.76 | 可编程 Guardrail |
| 4 | [Invariant](https://github.com/invariantlabs-ai/invariant) | 476 | +0 | 20 | 33.71 | 近期活跃度需继续复核 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | +1058.0 | +4.43% | 87.65 |
| 2 | [PyRIT](https://github.com/microsoft/PyRIT) | +49.0 | +1.04% | 64.25 |
| 3 | [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | +46.0 | +0.62% | 59.74 |

#### 新发现观察池

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)：2042 Stars；匹配度 3；Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪
- [secureagentics/Adrian](https://github.com/secureagentics/Adrian)：589 Stars；匹配度 3；Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts.
- [Agent-Threat-Rule/agent-threat-rules](https://github.com/Agent-Threat-Rule/agent-threat-rules)：427 Stars；匹配度 3；Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents. Executable, testable rules for prompt injection, tool poisoning, context exfiltration and MCP attacks. Merged into open-source projects at Microsoft, Cisco, Gen Digital, MISP and FINOS. MIT-licensed.
- [CyberSunil/LLMVault](https://github.com/CyberSunil/LLMVault)：353 Stars；匹配度 3；An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection, RAG Security, Agent Security, and GenAI penetration testing.
- [precize/Agentic-AI-Top10-Vulnerability](https://github.com/precize/Agentic-AI-Top10-Vulnerability)：204 Stars；匹配度 3；Top 10 for Agentic AI (AI Agent Security) serves as the core for OWASP and CSA Red teaming work

### Identity / Authorization

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Logto](https://github.com/logto-io/logto) | 14.9k | +38 | 100 | 77.55 | AI App 身份认证与授权底座 |
| 2 | [OpenFGA](https://github.com/openfga/openfga) | 6.1k | +44 | 100 | 76.89 | Agent/Skill/Tool/Resource 关系授权 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | 14.8k | +56 | 100 | 71.27 | Agent-first IAM 与网关 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [OpenFGA](https://github.com/openfga/openfga) | +44.0 | +0.72% | 63.31 |
| 2 | [Logto](https://github.com/logto-io/logto) | +38.0 | +0.26% | 62.42 |
| 3 | [Casdoor](https://github.com/casdoor/casdoor) | +56.0 | +0.38% | 60.84 |

#### 新发现观察池

- [zalando-incubator/agentic-identity-broker](https://github.com/zalando-incubator/agentic-identity-broker)：71 Stars；匹配度 3；Identity broker for AI agents with OAuth2 delegation and consent management
- [opena2a-org/agent-identity-management](https://github.com/opena2a-org/agent-identity-management)：67 Stars；匹配度 3；The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for non-human identities.
- [unicity-aos/capsule-identity](https://github.com/unicity-aos/capsule-identity)：8403 Stars；匹配度 2；System prompt builder. Assembles agent identity from workspace config and spark.toml. Part of Unicity AOS.
- [MetapriseAI/OrgKernel](https://github.com/MetapriseAI/OrgKernel)：2671 Stars；匹配度 2；Open-source trust layer for AI agents — cryptographic agent identity (Ed25519), instance-scoped execution tokens, SHA-256 hash-chained audit logging, and enterprise SSO/SCIM federation. The security foundation powering every agent in the Metaprise AURA platform.
- [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity)：757 Stars；匹配度 2；无仓库描述

### HITL / Agent UI

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 38.6k | +116 | 100 | 82.43 | Agent 前端和 AG-UI 实现 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | 13.0k | +125 | 100 | 73.93 | React Agent UI 组件库 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | 12.8k | +95 | 100 | 72.90 | 复杂编码任务的人机协作样本 |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | +116.0 | +0.30% | 68.90 |
| 2 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | +125.0 | +0.97% | 65.92 |
| 3 | [HumanLayer](https://github.com/humanlayer/humanlayer) | +95.0 | +0.75% | 64.08 |

#### 新发现观察池

- [virattt/financial-agent-ui](https://github.com/virattt/financial-agent-ui)：795 Stars；匹配度 1；Financial agent + generative UI
- [pacifio/ui](https://github.com/pacifio/ui)：154 Stars；匹配度 1；The shadcn for agent UI. A framework-agnostic design language for dense, AMOLED-black, multi-surface interfaces

### Agent Harness / Full Platform

#### 综合 Top 5

| 排名 | 项目 | Stars | 周增量 | 活跃度 | 综合分 | 研究定位 |
|---:|---|---:|---:|---:|---:|---|
| 1 | [Codex](https://github.com/openai/codex) | 134.0k | +1227 | 100 | 90.92 | 完整 Coding Agent Harness 源码样本 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | 225.6k | +1670 | 100 | 90.75 | 终端 Agent 架构参考 |
| 3 | [OpenHands](https://github.com/OpenHands/OpenHands) | 93.0k | +526 | 100 | 88.59 | 软件 Agent 执行与评测 |
| 4 | [DeerFlow](https://github.com/bytedance/deer-flow) | 85.2k | +306 | 100 | 86.66 | 长任务 SuperAgent 的完整拼装 |
| 5 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 261.8k | +2255 | 100 | 83.37 | 长期状态与可成长个人 Agent |

#### 本周增长 Top 5

| 排名 | 项目 | 周 Stars 增量 | 周增速 | 动量分 |
|---:|---|---:|---:|---:|
| 1 | [Codex](https://github.com/openai/codex) | +1227.0 | +0.92% | 81.85 |
| 2 | [OpenCode](https://github.com/anomalyco/opencode) | +1670.0 | +0.75% | 81.49 |
| 3 | [herdr](https://github.com/herdrdev/herdr) | +2118.0 | +4.47% | 80.82 |
| 4 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | +2255.0 | +0.87% | 77.99 |
| 5 | [OpenHands](https://github.com/OpenHands/OpenHands) | +526.0 | +0.57% | 77.83 |

#### 新发现观察池

- [xai-org/grok-build](https://github.com/xai-org/grok-build)：27723 Stars；匹配度 3；SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.
- [1jehuang/jcode](https://github.com/1jehuang/jcode)：21630 Stars；匹配度 3；High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：299817 Stars；匹配度 2；The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)：81304 Stars；匹配度 2；🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)：80095 Stars；匹配度 2；Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

## 数据质量与风险

- 正式候选池全部刷新成功。
- 新发现项目不会自动进入正式榜单，需人工确认模块边界、代码成熟度和许可证。
- `需复核`、`Custom`、强 copyleft 许可证项目在企业引入前必须单独审查。

## 下一步人工动作

1. 复核观察池中是否有值得加入正式候选池的新项目。
2. 对排名显著上升的项目检查 release、核心提交和架构变化，不能只解释 Stars。
3. 对长期不活跃、归档、改名或许可证变化的项目调整 P0/P1/P2。
