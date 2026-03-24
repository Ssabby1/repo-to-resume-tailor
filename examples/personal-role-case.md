# Personal Case: Target Role Mode

## Input

Repository:

`D:\graduate_design_graphrag\`

Target role:

`AI / Agent Development`

Prompt:

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description in Chinese for an AI / Agent development role. Output a short evidence analysis first, then one final version only. Include a dedicated tech stack line and do not invent unsupported Agent capabilities.
```

## Output

Analysis:
- Primary evidence came from `README.md`, `docs/architecture.md`, `docs/data_model.md`, `backend/app/services/*`, `backend/app/retrieval/*`, `backend/app/repositories/*`, `scripts/import_data.py`, and `backend/tests/*`.
- The project best matches GraphRAG or RAG system development, LLM integration and fallback design, retrieval orchestration, Neo4j graph applications, API delivery, and testing support.
- Strongly supported claims include the GraphRAG query path, hybrid retrieval with rerank, Neo4j graph modeling, FastAPI APIs, LLM fallback, and test coverage. More conservative wording should be used for planner or Agent-related parts because the repository does not fully support describing it as a complete multi-agent framework.

Resume version:

Project name: GraphRAG Learning Path Recommendation System  
Project positioning: An AI application for knowledge-graph-enhanced Q and A and learning-path recommendation, combining prerequisite graph reasoning, hybrid retrieval, and LLM generation to produce traceable learning suggestions.  
Tech stack: GraphRAG, FastAPI, Neo4j, LangChain, Hybrid Retrieval, Rerank

- Designed and implemented a GraphRAG query flow that connects subgraph retrieval, topological ordering, hybrid recall, and answer generation to output structured results with path, evidence, and citations.
- Built a Neo4j-based course knowledge graph and prerequisite relations, and encapsulated repository and import workflows to support graph queries and prerequisite closure retrieval.
- Implemented graph-plus-vector hybrid retrieval with RRF fusion and rerank to improve evidence recall quality while preserving source, score, and citation information for explainability.
- Integrated LLM-based request parsing and explanation generation, and added fallback, retry, and API or retrieval tests to improve service stability and iteration reliability.
