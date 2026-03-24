# 个人案例：具体 JD 模式

## 输入

仓库：

`D:\graphrag\`

具体岗位 JD：

字节跳动数据平台前端团队实习岗位，JD 重点包括：
- AI Agent 应用设计与优化
- 前端开发与用户体验
- AI 能力接入现有平台
- 技术调研与工程化实践
- React 或 Vue、基础后端知识、LLM、Prompt Engineering、LangChain、RAG、Function Calling 等方向

Prompt：

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description in Chinese tailored to this ByteDance AI full-stack internship JD. Output a short evidence analysis first, then one final version only. Include a dedicated tech stack line, prioritize frontend plus AI integration plus engineering evidence, and avoid overstating Agent capabilities.
```

## 输出

分析：
- 主要依据了 `README.md`、`docs/architecture.md`、`docs/api.md`、`frontend/package.json`、`frontend/src/views/GraphView.vue`、`backend/app/services/graphrag_service.py`、`backend/app/retrieval/hybrid_retriever.py`、`backend/app/services/planner_service.py` 和测试文件。
- 这个项目与 JD 的匹配点主要集中在前端交互开发、AI 应用集成、全栈 API 联调和工程化测试。
- 证据较强的部分包括 Vue 前端、FastAPI 后端、GraphRAG 与 Hybrid Retrieval 链路、LLM 解释与请求解析能力，以及接口测试；“Agent”相关表述需要保守，更适合写成 AI / Agent 场景探索，而不是完整 Agent 框架。

简历版本：

项目名称：GraphRAG Learning Path  
项目定位：面向知识图谱学习规划的 AI 应用项目，结合前端交互、检索编排与后端服务交付，支持可解释的学习建议生成。  
技术栈：Vue 3、Vite、ECharts、FastAPI、GraphRAG、Neo4j

- 设计并实现基于 Vue 3 的学习规划前端，支持知识点检索、路径生成、图谱可视化与多语言交互，完成前后端 API 联调。
- 基于 FastAPI 构建学习路径推荐与 GraphRAG 问答服务，打通从用户输入、检索编排到结果返回的完整应用链路。
- 实现图谱与向量混合检索流程，结合 RRF 与 rerank 输出包含 evidence 和 citations 的可解释结果，支撑 AI 应用与 Agent 场景探索。
- 补充请求解析、解释生成与接口 / 检索测试，增强工程化完整度与迭代稳定性。
