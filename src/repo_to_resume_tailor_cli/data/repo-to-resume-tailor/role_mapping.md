# Role Mapping Reference

Use this reference when matching repository evidence to a target role direction or a specific job description. If a role is not directly covered, classify it into the nearest category by underlying responsibilities rather than by title wording.

If a concrete job description is provided:
- treat repeated responsibilities as the highest-priority extraction signal
- treat repeated technical keywords as the highest-priority stack signal
- treat explicit delivery expectations as the highest-priority phrasing signal
- use the categories below as a fallback structure, not as a replacement for the job description

Do not fabricate technologies, responsibilities, ownership, or outcomes that the repository does not support.

## Tech Stack Priority Templates

Use these templates when generating the dedicated tech stack line. Do not list every technology found in the repository. Prefer 4 to 6 high-signal items, ordered by role relevance and hiring value.

General rules:
- prefer technologies with direct evidence in code, config, imports, runtime wiring, or deployment files
- prefer a mix of capability words and framework or infrastructure names when that makes the role fit clearer
- avoid listing low-signal utilities unless they are central to the target role
- avoid duplicate abstraction levels such as listing both a generic category and several weak examples unless the examples are strongly evidenced
- if the repository supports fewer than 4 solid items, output fewer rather than guessing

### AI / LLM / Agent

Preferred order:
1. capability words such as RAG, agent workflow, tool calling, multi-agent, evaluation
2. orchestration or framework words such as LangGraph, LangChain, LlamaIndex
3. service layer words such as FastAPI or inference service framework
4. retrieval or storage infrastructure such as vector database, retriever, reranker
5. model SDK or provider when directly evidenced

Recommended shape:
- capability plus framework plus service plus retrieval
- example: `RAG, LangGraph, FastAPI, Milvus, OpenAI SDK`

Avoid:
- listing only generic Python libraries when stronger AI workflow evidence exists
- hiding RAG or agent workflow inside prose while surfacing only web framework names

### Backend

Preferred order:
1. primary backend framework or runtime
2. database or ORM
3. cache or queue
4. auth, gateway, or service-support middleware when strongly evidenced
5. deployment or containerization layer

Recommended shape:
- framework plus data layer plus runtime support plus deployment
- example: `FastAPI, PostgreSQL, Redis, Celery, Docker`

Avoid:
- listing frontend tooling ahead of service runtime
- overloading the stack line with every middleware package

### Frontend

Preferred order:
1. primary frontend framework
2. language and build stack if central
3. state management or routing
4. UI or visualization layer when important
5. engineering or performance tooling when strongly evidenced

Recommended shape:
- framework plus language plus state or route plus UI or charting
- example: `React, TypeScript, Vite, Zustand, ECharts`

Avoid:
- listing minor utility libraries instead of core page or component stack
- treating lint or format tools as primary stack items unless engineering is the key story

### Full-stack

Preferred order:
1. frontend framework
2. backend framework
3. database
4. auth or API integration layer when central
5. deployment or containerization

Recommended shape:
- front plus back plus data plus delivery
- example: `Next.js, NestJS, PostgreSQL, JWT Auth, Docker`

Avoid:
- giving only one side of the stack when both are clearly evidenced
- listing too many frontend-only or backend-only details without showing the end-to-end nature

When a concrete job description is provided, override these templates if the JD repeatedly emphasizes a narrower subset, such as only retrieval, only deployment, or only data pipeline capability.

## 1. Backend / Server / Platform Application Development

Focus on:
- API design and endpoint implementation
- database modeling, SQL, and transaction handling
- Redis and cache design
- message queues, async jobs, and schedulers
- auth, permissions, and user systems
- logging, monitoring, and exception handling
- microservices, service split, and gateways
- Docker, deployment, and runtime delivery

Common evidence:
- `controller`, `service`, `dao`, `repository`
- SQL, ORM usage, cache config, MQ config
- `Dockerfile`, compose files, `nginx`, CI or CD files

## 2. Frontend / Web Frontend

Focus on:
- page and component design
- state management
- interaction implementation and API integration
- frontend engineering and build tooling
- auth routes, forms, and data visualization
- performance and maintainability

Common evidence:
- `components`, `pages`, `views`, `router`, `store`
- Vite, Webpack, ESLint, TypeScript
- charting code, rich interactions, lazy loading, reusable hooks

## 3. Full-stack

Focus on:
- full front-to-back product flow
- API design and data flow
- login, auth, and business loop closure
- deployment and environment configuration
- complete system implementation ability

Common evidence:
- both frontend and backend directories exist
- API call chains, database code, and deployment scripts are all present

## 4. Mobile / Android / iOS / Cross-platform Mobile

Focus on:
- page structure and user interaction
- local storage and network requests
- state management and component reuse
- performance optimization, adaptation, and packaging
- collaboration with backend APIs

Common evidence:
- Android or iOS project files
- Flutter, React Native, uni-app, or Taro
- routing, network layer, and state layer code

## 5. Test Development / QA Automation

Focus on:
- automated testing frameworks
- unit, integration, and API tests
- test data generation and coverage
- CI or CD testing integration
- quality assurance workflow

Common evidence:
- `test`, `tests`, `e2e`, `mock`
- `pytest`, `junit`, `jest`, `playwright`, `cypress`
- pipeline test steps

## 6. DevOps / SRE / Cloud Native

Focus on:
- automated deployment
- containerization and orchestration
- monitoring, alerting, and logging systems
- service reliability and recovery
- CI or CD, environment management, and release flow

Common evidence:
- `Dockerfile`, `docker-compose`, Kubernetes, Helm
- GitHub Actions, GitLab CI, Jenkins
- Prometheus, Grafana, ELK, Nginx, Terraform

## 7. Data Development / Data Engineering

Focus on:
- ETL or ELT flows
- data cleaning, transformation, and warehouse ingestion
- scheduling and batch processing
- warehouse modeling
- SQL development and data pipeline construction

Common evidence:
- Airflow, dbt, Spark, Flink, Hive
- SQL scripts, scheduling config, DAG definitions
- table schemas and metric-spec docs

## 8. Data Analysis

Focus on:
- data cleaning and analysis flow
- metric system construction
- visualization dashboards
- A or B test analysis
- business conclusion extraction

Common evidence:
- notebooks, BI reports, SQL, pandas, visualization code
- metric definitions, experiment analysis, conclusion docs

## 9. Algorithm / Machine Learning / Deep Learning

Focus on:
- data preprocessing and feature engineering
- model training and tuning
- evaluation metrics and experiment design
- inference deployment and service exposure
- result analysis and optimization

Common evidence:
- `train`, `infer`, `eval`, `dataset`, `metrics`
- PyTorch, TensorFlow, scikit-learn, XGBoost
- experiment config, checkpoints, inference endpoints

## 10. AI / LLM / Agent Development

Focus on:
- model integration and inference services
- prompt design and context organization
- RAG, vector retrieval, and knowledge QA
- tool calling, function calling, and workflow orchestration
- multi-agent collaboration, evaluation, and optimization
- result tracing, observability, and safety controls

Common evidence:
- LangChain, LangGraph, LlamaIndex, FastAPI
- vector databases, embeddings, retrievers, rerankers
- `tool`, `agent`, `workflow`, `memory`, `eval`, `trace`

## 11. Recommendation / Search / Ads Algorithms

Focus on:
- recall, ranking, and reranking
- feature engineering and sample construction
- offline training and online inference
- metric evaluation such as CTR, AUC, or NDCG
- search indexing, retrieval strategy, and ad logic

Common evidence:
- `recall`, `rank`, `rerank`, `feature`, `candidate`
- Elasticsearch, Faiss, ANN, ranking models
- metric scripts and experiment configs

## 12. Client / Desktop / Cross-platform App

Focus on:
- local feature implementation
- UI interaction and state flow
- system capability access
- local data management and sync
- packaging and distribution

Common evidence:
- Electron, Qt, C# WPF, Tauri
- local file handling, IPC, and system API calls

## 13. Security / Cybersecurity

Focus on:
- access control and security strategy
- vulnerability detection and protection
- attack-surface analysis
- audit logs and risk control mechanisms
- identity, encryption, and network security implementation

Common evidence:
- `auth`, `crypto`, `audit`, `filter`, `waf`
- scanners, rule engines, security middleware, access control

## 14. Game Development

Focus on:
- core gameplay implementation
- game logic and state machines
- UI, level, and asset management
- performance optimization and event systems
- networking, save systems, or client interactions

Common evidence:
- Unity, Unreal, Cocos
- `scene`, `entity`, `state`, `event`, `input`, `physics`

## 15. Technical Product / Product Planning

Focus on:
- requirement breakdown and feature structure
- prototype and process design
- technical solution collaboration
- data feedback loops
- project progress and cross-role coordination

Common evidence:
- PRD, flowcharts, API docs, tracking plans, analysis docs

Important note:
- Only extract this category when the repository clearly contains product docs, process artifacts, or planning materials. Do not force a pure code repository into a product-management framing.

## 16. Technical Project Management / RnD Coordination

Focus on:
- module split and task organization
- development process norms
- documentation and collaboration mechanisms
- continuous integration and delivery
- cross-role coordination traces

Common evidence:
- project docs, process specs, task templates, CI or CD, release records

Important note:
- Only express project-management capability when the repository contains explicit management traces. Do not infer management responsibilities from ordinary code structure alone.

## 17. AI Product Manager / AI Product / LLM Product / Agent Product

Focus on:
- product scenario definition and problem breakdown
- user-flow design and feature-structure design
- mapping LLM capabilities to business or product requirements
- how prompt, RAG, agent, or workflow capabilities land in concrete product features
- evaluation design, experience optimization, and feedback-loop closure
- feature boundaries, fallback behavior, safety, and controllability design
- cross-functional collaboration, requirement pushing, and iteration strategy

Common evidence:
- README or docs describing scenarios, target users, user flows, or product goals
- PRD, flowcharts, feature specs, evaluation docs, or solution-comparison docs
- API or workflow modules that clearly represent product flow rather than only infrastructure
- fallback, permission control, citation tracing, result explanation, or feedback mechanisms
- explicit constraints on output quality, explainability, stability, or safety

Writing emphasis:
- explain what user or business problem the project tries to solve, what features were designed, and how AI capabilities were used to deliver them
- do not mechanically translate pure engineering implementation into product language
- do not only list low-level technologies; explain how the technology supports product goals and user experience
- if the repository mainly proves technical implementation but lacks clear product design, requirement analysis, or feedback-loop evidence, do not over-package it as an AI product project
- when both technical implementation and product evidence are strong, it is acceptable to express both AI product positioning and AI application or agent landing capability
