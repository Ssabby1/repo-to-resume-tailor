# Examples Reference

## Evidence Handling Example

Strong evidence:
- a README explicitly says the project is a fraud detection platform
- a Docker Compose file shows Redis and PostgreSQL
- route definitions and service files show authentication and async task processing

Safe wording:
- designed and implemented core API modules
- integrated Redis and PostgreSQL for application data flow
- added basic async task handling capabilities

Weak evidence:
- only directory names imply there may be a scheduler
- dependencies include a vector database library but no retrieval flow is visible

Safe wording:
- the repository suggests planned scheduling support
- the project includes dependencies related to vector retrieval

Unsafe wording to avoid:
- built a production-grade scheduling platform
- independently developed a full RAG engine

## Output Framing Example

General version:
- summarize project positioning, stack, and 2 to 3 high-value modules

Role-tailored version:
- backend: stress API, data, auth, cache, deployment
- AI or agent: stress model calls, prompt flow, retrieval, tool use, orchestration
- data: stress pipelines, SQL, scheduling, modeling, metrics
