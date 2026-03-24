# Cursor 适配说明

Cursor 可以把这个项目作为规则集来复用，而不一定需要原生 Codex skill 机制。

推荐做法：

- 将 `repo-to-resume-tailor/SKILL.md` 放入 project rule 或 agent rule
- 将 `repo-to-resume-tailor/references/prompt.md` 作为可复用长提示词
- 使用 `examples/` 中的案例验证输出质量

建议使用方式：

```text
Analyze this repository and write one resume-ready project description based only on repository evidence, tailored to the following role or JD, with a dedicated tech stack line.
```
