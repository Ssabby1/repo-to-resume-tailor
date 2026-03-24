# Personal Case: Specific JD Mode

## Input

Repository:

`D:\graphrag\`

Specific job description:

ByteDance data platform frontend team internship. The JD emphasizes:
- AI Agent application design and optimization
- frontend development and user experience
- AI integration into an existing platform
- technical research and engineering practices
- React or Vue, basic backend knowledge, LLM, Prompt Engineering, LangChain, RAG, and Function Calling awareness

Prompt:

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description in Chinese tailored to this ByteDance AI full-stack internship JD. Output a short evidence analysis first, then one final version only. Include a dedicated tech stack line, prioritize frontend plus AI integration plus engineering evidence, and avoid overstating Agent capabilities.
```

## Output

Analysis:
- Key evidence came from `README.md`, `docs/architecture.md`, `docs/api.md`, `frontend/package.json`, `frontend/src/views/GraphView.vue`, `backend/app/services/graphrag_service.py`, `backend/app/retrieval/hybrid_retriever.py`, `backend/app/services/planner_service.py`, and test files.
- The project best matches the JD's frontend interaction development, AI application integration, full-stack API collaboration, and engineering testing requirements.
- Strong evidence supports the Vue frontend, FastAPI backend, GraphRAG and hybrid retrieval path, LLM explanation and request parsing, and API testing. Agent wording should stay conservative because the repository is better described as AI or Agent scenario exploration rather than a full Agent framework.

Resume version:

Project name: GraphRAG Learning Path  
Project positioning: An AI application project for knowledge-graph-based learning planning, combining frontend interaction, retrieval orchestration, and backend service delivery to support explainable study guidance.  
Tech stack: Vue 3, Vite, ECharts, FastAPI, GraphRAG, Neo4j

- Designed and implemented a Vue 3 frontend for learning planning, supporting concept search, path generation, graph visualization, and multilingual interaction, and completed frontend-backend API integration.
- Built FastAPI services for learning path recommendation and GraphRAG question answering, connecting user input, retrieval orchestration, and result delivery into a complete application flow.
- Implemented graph-plus-vector hybrid retrieval with RRF and rerank to generate explainable outputs with evidence and citations, supporting AI application and Agent scenario exploration.
- Added request parsing, explanation generation, and interface or retrieval tests to strengthen engineering completeness and iteration stability.
