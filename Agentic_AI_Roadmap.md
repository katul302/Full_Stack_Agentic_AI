# 🤖 Full Agentic AI Roadmap & Duration

> A comprehensive, structured roadmap to go from beginner to expert in Agentic AI — covering foundations, core skills, frameworks, and real-world deployment.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Phase 1 — Foundations (Weeks 1–6)](#phase-1--foundations-weeks-16)
3. [Phase 2 — Machine Learning & Deep Learning (Weeks 7–14)](#phase-2--machine-learning--deep-learning-weeks-714)
4. [Phase 3 — Large Language Models (Weeks 15–20)](#phase-3--large-language-models-llms-weeks-1520)
5. [Phase 4 — Agentic AI Core Concepts (Weeks 21–26)](#phase-4--agentic-ai-core-concepts-weeks-2126)
6. [Phase 5 — Agentic Frameworks & Tools (Weeks 27–32)](#phase-5--agentic-frameworks--tools-weeks-2732)
7. [Phase 6 — Advanced Agentic Patterns (Weeks 33–38)](#phase-6--advanced-agentic-patterns-weeks-3338)
8. [Phase 7 — Production & Deployment (Weeks 39–44)](#phase-7--production--deployment-weeks-3944)
9. [Phase 8 — Specializations & Capstone Projects (Weeks 45–52)](#phase-8--specializations--capstone-projects-weeks-4552)
10. [Resources & Tools](#resources--tools)
11. [Duration Summary](#duration-summary)

---

## Overview

**Agentic AI** refers to AI systems that can autonomously plan, reason, use tools, and take multi-step actions to accomplish complex goals — going far beyond simple chatbots or single-turn LLM calls.

This roadmap takes you from zero to building production-grade AI agents in **~12 months** (part-time) or **~6 months** (full-time).

| Track | Hours/Week | Duration |
|-------|-----------|----------|
| 🐢 Part-time | 10–15 hrs/week | ~12 months |
| 🚀 Full-time | 30–40 hrs/week | ~6 months |
| ⚡ Intensive Bootcamp | 50+ hrs/week | ~3–4 months |

---

## Phase 1 — Foundations (Weeks 1–6)

> **Goal:** Build the programming and math foundation required for AI development.
> **Duration:** 6 weeks | ~80–100 hours total

### 1.1 Python Programming (Weeks 1–2)

| Topic | Hours |
|-------|-------|
| Python basics — variables, data types, control flow | 8 |
| Functions, scope, closures, decorators | 6 |
| OOP — classes, inheritance, dunder methods | 8 |
| File I/O, error handling, context managers | 4 |
| Python standard library (os, sys, json, re, datetime) | 4 |
| Virtual environments, pip, packaging | 2 |
| **Subtotal** | **~32 hrs** |

**Resources:**
- Python.org official docs
- "Automate the Boring Stuff with Python" — Al Sweigart (free online)
- CS50P — Harvard Python course (free)
- Real Python (realpython.com)

### 1.2 Mathematics for AI (Weeks 3–4)

| Topic | Hours |
|-------|-------|
| Linear Algebra — vectors, matrices, dot products, eigenvalues | 10 |
| Calculus — derivatives, gradients, chain rule | 8 |
| Probability & Statistics — distributions, Bayes theorem | 8 |
| Information Theory — entropy, KL divergence | 4 |
| **Subtotal** | **~30 hrs** |

**Resources:**
- 3Blue1Brown — "Essence of Linear Algebra" (YouTube, free)
- Khan Academy — Calculus & Statistics (free)
- "Mathematics for Machine Learning" — Deisenroth et al. (free PDF)

### 1.3 Data Manipulation & Visualization (Weeks 5–6)

| Topic | Hours |
|-------|-------|
| NumPy — arrays, broadcasting, vectorized operations | 6 |
| Pandas — DataFrames, groupby, merging, cleaning | 8 |
| Matplotlib & Seaborn — plotting & EDA | 6 |
| Jupyter Notebooks workflow | 2 |
| **Subtotal** | **~22 hrs** |

**Resources:**
- NumPy & Pandas official documentation
- Kaggle free courses (Pandas, Data Visualization)
- "Python for Data Analysis" — Wes McKinney

### ✅ Phase 1 Milestones
- [ ] Build a data analysis project using Pandas & NumPy
- [ ] Solve 20+ Python coding challenges (LeetCode Easy)
- [ ] Implement basic matrix operations from scratch
- [ ] Create visualizations from a real dataset

---

## Phase 2 — Machine Learning & Deep Learning (Weeks 7–14)

> **Goal:** Understand how models learn, and build intuition for neural networks.
> **Duration:** 8 weeks | ~120–150 hours total

### 2.1 Classical Machine Learning (Weeks 7–9)

| Topic | Hours |
|-------|-------|
| Supervised learning — regression, classification | 8 |
| Unsupervised learning — clustering, PCA | 6 |
| Decision Trees, Random Forests, Gradient Boosting | 8 |
| Model evaluation — cross-validation, metrics, overfitting | 6 |
| Scikit-learn pipeline & preprocessing | 6 |
| Feature engineering & selection | 4 |
| **Subtotal** | **~38 hrs** |

**Resources:**
- Scikit-learn official docs & user guide
- "Hands-On Machine Learning" — Aurélien Géron (O'Reilly)
- fast.ai ML course (free)

### 2.2 Deep Learning Fundamentals (Weeks 10–12)

| Topic | Hours |
|-------|-------|
| Neural network architecture — layers, activations, loss | 8 |
| Backpropagation & gradient descent (from scratch) | 6 |
| PyTorch basics — tensors, autograd, nn.Module | 10 |
| CNNs — image classification, feature maps | 8 |
| RNNs & LSTMs — sequence modeling | 6 |
| Regularization — dropout, batch norm, weight decay | 4 |
| **Subtotal** | **~42 hrs** |

**Resources:**
- fast.ai "Practical Deep Learning for Coders" (free)
- PyTorch official tutorials
- "Deep Learning" — Goodfellow, Bengio, Courville (free PDF)
- Andrej Karpathy's "Neural Networks: Zero to Hero" (YouTube)

### 2.3 Training & Optimization (Weeks 13–14)

| Topic | Hours |
|-------|-------|
| Optimizers — SGD, Adam, AdamW, learning rate schedules | 6 |
| Transfer learning & fine-tuning pretrained models | 8 |
| GPU training, mixed precision, gradient checkpointing | 6 |
| Experiment tracking — Weights & Biases, MLflow | 4 |
| Model saving, checkpointing, ONNX export | 4 |
| **Subtotal** | **~28 hrs** |

**Resources:**
- Weights & Biases docs & tutorials
- HuggingFace Transformers docs
- PyTorch Lightning docs

### ✅ Phase 2 Milestones
- [ ] Train a classifier on a real dataset (e.g., CIFAR-10 or tabular data)
- [ ] Implement a neural network from scratch in NumPy
- [ ] Fine-tune a pretrained model using HuggingFace
- [ ] Log experiments with W&B or MLflow

---

## Phase 3 — Large Language Models / LLMs (Weeks 15–20)

> **Goal:** Deeply understand how LLMs work, how to use them via APIs, and how to fine-tune them.
> **Duration:** 6 weeks | ~100–120 hours total

### 3.1 Transformer Architecture (Weeks 15–16)

| Topic | Hours |
|-------|-------|
| Attention mechanism — self-attention, multi-head attention | 8 |
| Transformer encoder & decoder architecture | 6 |
| Positional encoding, tokenization, embeddings | 6 |
| BERT, GPT, T5 — architecture differences | 6 |
| Reading key papers: "Attention Is All You Need", GPT-3 | 4 |
| **Subtotal** | **~30 hrs** |

**Resources:**
- "The Illustrated Transformer" — Jay Alammar (blog)
- Andrej Karpathy — "Let's build GPT from scratch" (YouTube)
- HuggingFace NLP course (free)

### 3.2 Working with LLM APIs (Weeks 17–18)

| Topic | Hours |
|-------|-------|
| OpenAI API — completions, chat, embeddings, function calling | 8 |
| Anthropic Claude API | 4 |
| Google Gemini API | 4 |
| Open-source models — Ollama, LM Studio, llama.cpp | 6 |
| Prompt engineering — zero-shot, few-shot, chain-of-thought | 8 |
| Token limits, context windows, cost optimization | 4 |
| **Subtotal** | **~34 hrs** |

**Resources:**
- OpenAI API docs & cookbook
- Anthropic prompt engineering guide
- Ollama.ai docs
- "Prompt Engineering Guide" — DAIR.AI (free)

### 3.3 Fine-tuning & Embeddings (Weeks 19–20)

| Topic | Hours |
|-------|-------|
| Fine-tuning with HuggingFace Trainer API | 8 |
| Parameter-efficient fine-tuning — LoRA, QLoRA, PEFT | 8 |
| Text embeddings — sentence-transformers, OpenAI embeddings | 6 |
| Vector databases — Pinecone, Weaviate, ChromaDB, FAISS | 6 |
| Retrieval-Augmented Generation (RAG) basics | 8 |
| **Subtotal** | **~36 hrs** |

**Resources:**
- HuggingFace PEFT docs
- LangChain RAG tutorials
- ChromaDB & Pinecone docs
- "Building RAG Applications" — various blog posts

### ✅ Phase 3 Milestones
- [ ] Build a chatbot using OpenAI API with conversation history
- [ ] Implement RAG pipeline with a vector database
- [ ] Fine-tune a small LLM (e.g., Mistral 7B) using LoRA
- [ ] Compare outputs from 3+ different LLM providers

---

## Phase 4 — Agentic AI Core Concepts (Weeks 21–26)

> **Goal:** Master the fundamental building blocks of AI agents — reasoning, planning, memory, and tool use.
> **Duration:** 6 weeks | ~100–120 hours total

### 4.1 What Makes an AI Agent? (Week 21)

| Topic | Hours |
|-------|-------|
| Agent vs. chatbot vs. automation — key distinctions | 3 |
| The agent loop: Perceive → Think → Act → Observe | 4 |
| Types of agents: reactive, deliberative, hybrid | 3 |
| Agent taxonomies: single-agent, multi-agent, hierarchical | 4 |
| Key papers: ReAct, Toolformer, AutoGPT analysis | 4 |
| **Subtotal** | **~18 hrs** |

### 4.2 Reasoning & Planning (Weeks 22–23)

| Topic | Hours |
|-------|-------|
| Chain-of-Thought (CoT) prompting | 4 |
| Tree-of-Thought (ToT) reasoning | 4 |
| ReAct pattern — Reasoning + Acting interleaved | 6 |
| Plan-and-Execute pattern | 4 |
| Self-reflection & self-critique loops | 4 |
| Task decomposition strategies | 4 |
| **Subtotal** | **~26 hrs** |

**Resources:**
- ReAct paper: "ReAct: Synergizing Reasoning and Acting in Language Models"
- Tree of Thoughts paper (Yao et al., 2023)
- LangChain agents documentation

### 4.3 Memory Systems (Week 24)

| Topic | Hours |
|-------|-------|
| Short-term memory — conversation buffers, sliding windows | 4 |
| Long-term memory — vector stores, episodic memory | 6 |
| Semantic memory — knowledge graphs, structured stores | 4 |
| Memory retrieval strategies — similarity, recency, importance | 4 |
| **Subtotal** | **~18 hrs** |

**Resources:**
- MemGPT paper
- LangChain memory modules docs
- Zep memory framework

### 4.4 Tool Use & Function Calling (Weeks 25–26)

| Topic | Hours |
|-------|-------|
| OpenAI function calling / tool use API | 6 |
| Designing tools — schemas, descriptions, error handling | 6 |
| Built-in tools: web search, code execution, file I/O | 6 |
| Custom tool creation patterns | 6 |
| Tool selection & routing strategies | 4 |
| Handling tool errors & retries gracefully | 4 |
| **Subtotal** | **~32 hrs** |

**Resources:**
- OpenAI function calling docs
- LangChain tools & toolkits docs
- Anthropic tool use guide

### ✅ Phase 4 Milestones
- [ ] Build a ReAct agent from scratch using raw LLM API calls
- [ ] Implement a multi-turn agent with persistent memory
- [ ] Create 5+ custom tools and integrate them into an agent
- [ ] Build an agent that can search the web and summarize results

---

## Phase 5 — Agentic Frameworks & Tools (Weeks 27–32)

> **Goal:** Master the leading agentic AI frameworks used in industry.
> **Duration:** 6 weeks | ~100–120 hours total

### 5.1 LangChain (Weeks 27–28)

| Topic | Hours |
|-------|-------|
| LangChain architecture — chains, runnables, LCEL | 6 |
| LangChain agents — AgentExecutor, tool binding | 6 |
| LangChain memory & conversation management | 4 |
| LangChain RAG — document loaders, splitters, retrievers | 6 |
| LangSmith — tracing, evaluation, debugging | 4 |
| **Subtotal** | **~26 hrs** |

**Resources:**
- LangChain official docs (python.langchain.com)
- LangChain cookbook & tutorials
- LangSmith docs

### 5.2 LangGraph (Week 29)

| Topic | Hours |
|-------|-------|
| Graph-based agent orchestration concepts | 4 |
| StateGraph — nodes, edges, conditional routing | 6 |
| Cycles, loops, and human-in-the-loop patterns | 4 |
| Persistence & checkpointing in LangGraph | 4 |
| Building complex multi-step workflows | 4 |
| **Subtotal** | **~22 hrs** |

**Resources:**
- LangGraph official docs
- LangGraph tutorials & examples on GitHub

### 5.3 CrewAI (Week 30)

| Topic | Hours |
|-------|-------|
| CrewAI architecture — agents, tasks, crews | 4 |
| Role-based agent design | 4 |
| Sequential vs. hierarchical process flows | 4 |
| Custom tools in CrewAI | 4 |
| Building a multi-agent research crew | 4 |
| **Subtotal** | **~20 hrs** |

**Resources:**
- CrewAI official docs (docs.crewai.com)
- CrewAI GitHub examples

### 5.4 AutoGen & Other Frameworks (Weeks 31–32)

| Topic | Hours |
|-------|-------|
| Microsoft AutoGen — conversational multi-agent patterns | 6 |
| AutoGen Studio — no-code agent builder | 4 |
| Semantic Kernel — Microsoft's agent SDK | 4 |
| Haystack — production NLP & agent pipelines | 4 |
| Comparing frameworks — when to use which | 4 |
| OpenAI Assistants API — threads, runs, file search | 6 |
| **Subtotal** | **~28 hrs** |

**Resources:**
- AutoGen docs (microsoft.github.io/autogen)
- Semantic Kernel docs
- OpenAI Assistants API docs

### ✅ Phase 5 Milestones
- [ ] Build a full RAG agent using LangChain + LangGraph
- [ ] Create a multi-agent crew with CrewAI for a research task
- [ ] Build a conversational multi-agent system with AutoGen
- [ ] Deploy an agent using OpenAI Assistants API

---

## Phase 6 — Advanced Agentic Patterns (Weeks 33–38)

> **Goal:** Build sophisticated, production-ready agent architectures.
> **Duration:** 6 weeks | ~100–120 hours total

### 6.1 Multi-Agent Systems (Weeks 33–34)

| Topic | Hours |
|-------|-------|
| Multi-agent orchestration patterns | 6 |
| Supervisor / worker agent hierarchies | 6 |
| Agent communication protocols & message passing | 4 |
| Conflict resolution & consensus mechanisms | 4 |
| Parallelism & async agent execution | 6 |
| **Subtotal** | **~26 hrs** |

**Resources:**
- LangGraph multi-agent tutorials
- AutoGen group chat patterns
- "Generative Agents" paper (Park et al., 2023)

### 6.2 Human-in-the-Loop (HITL) Patterns (Week 35)

| Topic | Hours |
|-------|-------|
| When and why to include human oversight | 3 |
| Approval gates & interrupt patterns | 4 |
| Feedback loops — human corrections to agent state | 4 |
| Escalation strategies for uncertain decisions | 3 |
| Building HITL workflows in LangGraph | 4 |
| **Subtotal** | **~18 hrs** |

### 6.3 Agent Evaluation & Testing (Week 36)

| Topic | Hours |
|-------|-------|
| Evaluating agent trajectories & final outputs | 4 |
| LLM-as-judge evaluation patterns | 4 |
| Unit testing tools and agent steps | 4 |
| Regression testing for agent behavior | 4 |
| Benchmarking agents — GAIA, AgentBench, WebArena | 4 |
| **Subtotal** | **~20 hrs** |

**Resources:**
- LangSmith evaluation docs
- GAIA benchmark paper
- "Evaluating LLM Agents" — various blog posts

### 6.4 Advanced RAG & Knowledge Systems (Weeks 37–38)

| Topic | Hours |
|-------|-------|
| Advanced RAG — HyDE, multi-query, parent-child chunking | 8 |
| Graph RAG — knowledge graphs + vector search | 6 |
| Agentic RAG — agents that decide when/how to retrieve | 6 |
| Structured data agents — SQL, APIs, spreadsheets | 6 |
| Multimodal agents — vision, audio, documents | 6 |
| **Subtotal** | **~32 hrs** |

**Resources:**
- LlamaIndex advanced RAG docs
- Microsoft GraphRAG
- GPT-4V & multimodal API docs

### ✅ Phase 6 Milestones
- [ ] Build a supervisor + worker multi-agent pipeline
- [ ] Implement a HITL approval workflow for a critical task
- [ ] Evaluate an agent using LLM-as-judge on 50+ test cases
- [ ] Build a Graph RAG system over a custom knowledge base

---

## Phase 7 — Production & Deployment (Weeks 39–44)

> **Goal:** Ship agents to production with reliability, observability, and security.
> **Duration:** 6 weeks | ~100–120 hours total

### 7.1 API Design & Backend Integration (Weeks 39–40)

| Topic | Hours |
|-------|-------|
| FastAPI — building REST APIs for agent backends | 8 |
| WebSockets & streaming responses for agents | 6 |
| Authentication & authorization (JWT, OAuth2) | 4 |
| Rate limiting, throttling, and quota management | 4 |
| Async Python — asyncio, aiohttp for concurrent agents | 6 |
| **Subtotal** | **~28 hrs** |

**Resources:**
- FastAPI official docs
- Python asyncio docs
- "Building APIs with FastAPI" — various tutorials

### 7.2 Containerization & Cloud Deployment (Weeks 41–42)

| Topic | Hours |
|-------|-------|
| Docker — containerizing agent applications | 6 |
| Docker Compose — multi-service agent stacks | 4 |
| Kubernetes basics — pods, services, deployments | 6 |
| Cloud deployment — AWS, GCP, Azure (choose one) | 8 |
| Serverless agents — AWS Lambda, Google Cloud Run | 4 |
| CI/CD pipelines — GitHub Actions for agent apps | 4 |
| **Subtotal** | **~32 hrs** |

**Resources:**
- Docker official docs
- AWS/GCP/Azure free tier tutorials
- GitHub Actions docs

### 7.3 Observability & Monitoring (Week 43)

| Topic | Hours |
|-------|-------|
| Logging agent actions, decisions, and tool calls | 4 |
| Distributed tracing — OpenTelemetry for agents | 4 |
| LangSmith / Langfuse for LLM observability | 4 |
| Cost monitoring & token usage dashboards | 3 |
| Alerting on agent failures & anomalies | 3 |
| **Subtotal** | **~18 hrs** |

**Resources:**
- LangSmith docs
- Langfuse open-source observability
- OpenTelemetry Python docs

### 7.4 Safety, Security & Guardrails (Week 44)

| Topic | Hours |
|-------|-------|
| Prompt injection attacks & defenses | 4 |
| Output validation & structured output enforcement | 4 |
| Guardrails AI & NeMo Guardrails | 4 |
| Data privacy — PII detection & redaction | 4 |
| Agent sandboxing — restricting dangerous actions | 4 |
| Responsible AI principles for agentic systems | 2 |
| **Subtotal** | **~22 hrs** |

**Resources:**
- Guardrails AI docs
- NVIDIA NeMo Guardrails
- OWASP LLM Top 10

### ✅ Phase 7 Milestones
- [ ] Deploy a production agent API using FastAPI + Docker
- [ ] Set up full observability with LangSmith or Langfuse
- [ ] Implement prompt injection defenses and output guardrails
- [ ] Deploy to cloud with auto-scaling and CI/CD pipeline

---

## Phase 8 — Specializations & Capstone Projects (Weeks 45–52)

> **Goal:** Pick a specialization track and build a portfolio-worthy capstone project.
> **Duration:** 8 weeks | ~120–160 hours total

### 8.1 Choose Your Specialization Track (Weeks 45–46)

Pick **one or more** tracks based on your career goals:

#### 🔬 Track A — Research & Reasoning Agents
| Topic | Hours |
|-------|-------|
| Reinforcement Learning from Human Feedback (RLHF) | 8 |
| Constitutional AI & self-alignment techniques | 6 |
| Agent self-improvement & meta-learning | 6 |
| Reading & implementing recent agent papers | 8 |
| **Subtotal** | **~28 hrs** |

#### 💼 Track B — Enterprise & Workflow Automation Agents
| Topic | Hours |
|-------|-------|
| Business process automation with agents | 6 |
| Integration with enterprise tools (Slack, Jira, Salesforce) | 6 |
| Document processing agents (PDFs, contracts, invoices) | 6 |
| Email & calendar agents | 4 |
| **Subtotal** | **~22 hrs** |

#### 🖥️ Track C — Coding & Software Engineering Agents
| Topic | Hours |
|-------|-------|
| Code generation & review agents | 6 |
| Autonomous debugging & test-writing agents | 6 |
| GitHub integration — PR review, issue triage agents | 6 |
| SWE-bench & coding agent benchmarks | 4 |
| **Subtotal** | **~22 hrs** |

#### 🌐 Track D — Web & Browser Agents
| Topic | Hours |
|-------|-------|
| Browser automation — Playwright, Selenium with LLMs | 6 |
| Web scraping agents with dynamic content | 4 |
| Computer use agents (Anthropic, OpenAI CUA) | 6 |
| GUI agents — controlling desktop applications | 4 |
| **Subtotal** | **~20 hrs** |

### 8.2 Capstone Project (Weeks 47–52)

Build a **complete, production-grade agentic AI system** from scratch.

| Activity | Hours |
|----------|-------|
| Project planning & architecture design | 8 |
| Core agent implementation | 20 |
| Tool & integration development | 12 |
| Testing, evaluation & iteration | 10 |
| Deployment & documentation | 8 |
| Demo video & portfolio write-up | 6 |
| **Subtotal** | **~64 hrs** |

**Capstone Project Ideas:**
- 🔍 **Research Agent** — autonomously researches a topic, synthesizes sources, writes a report
- 💻 **Coding Assistant Agent** — reviews PRs, writes tests, fixes bugs autonomously
- 📊 **Data Analysis Agent** — connects to databases, runs queries, generates insights & charts
- 🛒 **E-commerce Agent** — handles customer queries, checks inventory, processes orders
- 📰 **News Aggregator Agent** — monitors sources, summarizes, personalizes daily briefings
- 🏥 **Healthcare Triage Agent** — routes patient queries, schedules appointments, checks records

### ✅ Phase 8 Milestones
- [ ] Complete chosen specialization track
- [ ] Build and deploy capstone project end-to-end
- [ ] Write technical blog post or README documenting the project
- [ ] Publish project to GitHub with full documentation
- [ ] Record a demo video showcasing the agent in action

---

## Resources & Tools

### 🛠️ Essential Tools & Libraries

| Category | Tools |
|----------|-------|
| **LLM APIs** | OpenAI, Anthropic, Google Gemini, Cohere, Mistral |
| **Open-source LLMs** | Ollama, LM Studio, llama.cpp, vLLM |
| **Agent Frameworks** | LangChain, LangGraph, CrewAI, AutoGen, Semantic Kernel |
| **Vector Databases** | ChromaDB, Pinecone, Weaviate, FAISS, Qdrant |
| **Observability** | LangSmith, Langfuse, OpenTelemetry, W&B |
| **Deployment** | FastAPI, Docker, Kubernetes, AWS/GCP/Azure |
| **Guardrails** | Guardrails AI, NeMo Guardrails, Rebuff |
| **Evaluation** | RAGAS, DeepEval, LangSmith Evals |

### 📚 Must-Read Papers

1. "Attention Is All You Need" — Vaswani et al. (2017)
2. "GPT-3: Language Models are Few-Shot Learners" — Brown et al. (2020)
3. "ReAct: Synergizing Reasoning and Acting in Language Models" — Yao et al. (2022)
4. "Toolformer: Language Models Can Teach Themselves to Use Tools" — Schick et al. (2023)
5. "Generative Agents: Interactive Simulacra of Human Behavior" — Park et al. (2023)
6. "Tree of Thoughts: Deliberate Problem Solving with LLMs" — Yao et al. (2023)
7. "MemGPT: Towards LLMs as Operating Systems" — Packer et al. (2023)
8. "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" — Wu et al. (2023)

### 🎓 Free Learning Platforms

- **DeepLearning.AI** (deeplearning.ai) — Short courses on LLMs, agents, RAG
- **fast.ai** — Practical deep learning & ML
- **HuggingFace** — NLP course, model hub, spaces
- **Kaggle** — Datasets, competitions, free courses
- **Coursera / edX** — Structured university courses
- **YouTube** — Andrej Karpathy, Yannic Kilcher, AI Explained

---

## Duration Summary

### ⏱️ Phase-by-Phase Time Breakdown

| Phase | Topic | Weeks | Est. Hours |
|-------|-------|-------|-----------|
| 1 | Foundations (Python, Math, Data) | 1–6 | ~90 hrs |
| 2 | Machine Learning & Deep Learning | 7–14 | ~130 hrs |
| 3 | Large Language Models (LLMs) | 15–20 | ~110 hrs |
| 4 | Agentic AI Core Concepts | 21–26 | ~110 hrs |
| 5 | Agentic Frameworks & Tools | 27–32 | ~100 hrs |
| 6 | Advanced Agentic Patterns | 33–38 | ~110 hrs |
| 7 | Production & Deployment | 39–44 | ~100 hrs |
| 8 | Specializations & Capstone | 45–52 | ~140 hrs |
| **Total** | | **52 weeks** | **~890 hrs** |

### 🗓️ Realistic Timeline Estimates

| Commitment Level | Hours/Week | Total Duration |
|-----------------|-----------|----------------|
| Casual learner | 5–8 hrs | ~2–3 years |
| Part-time | 10–15 hrs | ~12–18 months |
| Full-time | 30–40 hrs | ~5–7 months |
| Intensive bootcamp | 50–60 hrs | ~3–4 months |

### 🎯 Skill Level Checkpoints

| After Phase | Skill Level | What You Can Build |
|-------------|-------------|-------------------|
| Phase 1–2 | Beginner | Data pipelines, ML models |
| Phase 3 | Intermediate | LLM-powered chatbots, RAG apps |
| Phase 4–5 | Advanced | Single & multi-agent systems |
| Phase 6–7 | Expert | Production-grade agent platforms |
| Phase 8 | Specialist | Domain-specific agentic products |

---

> 💡 **Pro Tips:**
> - **Build as you learn** — every concept should have a hands-on project
> - **Join communities** — AI Discord servers, Twitter/X AI community, Reddit r/MachineLearning
> - **Stay current** — the field moves fast; follow arXiv, AI newsletters (The Batch, TLDR AI)
> - **Contribute to open source** — LangChain, CrewAI, AutoGen all welcome contributors
> - **Document everything** — your GitHub portfolio is your resume in this field

---

*Last updated: April 2026 | Roadmap version 1.0*
