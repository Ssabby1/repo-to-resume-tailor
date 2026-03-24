# 个人案例：目标岗位模式

## 输入

仓库：

`D:\graphrag\`

目标岗位：

`AI / Agent 开发`

Prompt：

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description in Chinese for an AI / Agent development role. Output a short evidence analysis first, then one final version only. Include a dedicated tech stack line and do not invent unsupported Agent capabilities.
```

## 输出

分析：
- 主要依据了 `README.md`、`docs/architecture.md`、`docs/data_model.md`、`backend/app/services/*`、`backend/app/retrieval/*`、`backend/app/repositories/*`、`scripts/import_data.py` 和 `backend/tests/*`。
- 这个项目最匹配 GraphRAG / RAG 系统开发、LLM 接入与 fallback 设计、检索编排、Neo4j 图谱应用、API 化交付与测试保障。
- 证据最强的点包括 GraphRAG 查询链路、混合检索与 rerank、Neo4j 图模型、FastAPI 接口、LLM fallback 和测试覆盖。对于 planner 或 Agent 相关能力，需要保持保守表述，因为仓库还不足以支撑“完整多 Agent 框架”这类说法。

简历版本：

项目名称：GraphRAG 学习路径推荐系统  
项目定位：面向 AI 应用的知识图谱增强问答与学习路径推荐系统，结合先修图谱推理、混合检索与 LLM 生成，为用户输出可追溯的学习建议。  
技术栈：GraphRAG、FastAPI、Neo4j、LangChain、Hybrid Retrieval、Rerank

- 设计并实现 GraphRAG 查询链路，串联子图检索、拓扑排序、混合召回与答案生成，输出包含 path、evidence 和 citations 的结构化结果。
- 基于 Neo4j 构建课程知识图谱与先修关系，并封装 Repository 与数据导入流程，支持图谱查询与先修闭包检索。
- 实现图检索与向量检索融合方案，结合 RRF 融合与 rerank 提升证据召回质量，并保留来源、分数与引用信息增强可解释性。
- 接入 LLM 完成请求解析与解释生成，并补充 fallback、重试和 API / 检索测试，提升服务稳定性与迭代可靠性。
