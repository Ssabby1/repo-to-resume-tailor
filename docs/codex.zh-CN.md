# Codex 使用说明

## 安装

将内部的 `repo-to-resume-tailor/` 目录复制到 Codex 的 skills 目录中：

```text
~/.codex/skills/repo-to-resume-tailor/
```

安装后的目录应包含：

```text
SKILL.md
role_mapping.md
agents/openai.yaml
references/prompt.md
references/examples.md
```

## 使用方式

示例：

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description tailored to an AI engineer role, with a dedicated tech stack line.
```

你也可以直接提供具体岗位 JD，让它按 JD 改写项目描述。
