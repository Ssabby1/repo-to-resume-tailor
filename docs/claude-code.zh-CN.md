# Claude Code 适配说明

Claude Code 不使用和 Codex 完全相同的原生 skill 打包方式。可以复用以下文件内容：

- `repo-to-resume-tailor/SKILL.md`
- `repo-to-resume-tailor/role_mapping.md`
- `repo-to-resume-tailor/references/prompt.md`

推荐做法：

- 将规则整理成可复用的 prompt 模板
- 将长提示词保存为项目笔记或常用命令片段
- 保持“证据优先”和“禁止夸大”的规则不变

建议适配提示词：

```text
Analyze this repository and turn it into one resume-ready project description. Base every claim on repository evidence, rank details by target role or JD fit, output a short evidence analysis first, include a dedicated tech stack line, and do not invent metrics or unsupported ownership claims.
```
