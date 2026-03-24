# repo-to-resume-tailor

English | [中文](#中文说明)

`repo-to-resume-tailor` is a reusable skill and prompt package for turning a source code repository into a resume-ready project description. It analyzes repository evidence, matches the project against a target role or a specific job description, and produces concise, credible, hiring-oriented project text instead of a generic repository summary.

## Overview

This project is designed for two common resume-writing scenarios:

- target-role mode: the user provides a target role direction such as backend, frontend, AI or agent, data, full-stack, DevOps, or security
- JD mode: the user pastes a concrete job description and wants the project description tailored to it

The package is platform-friendly rather than platform-exclusive:

- on Codex, it can be used as a native skill
- on Claude Code, Cursor, or similar tools, it can be reused as a prompt and rules package

## What It Does

- analyze a full repository instead of a single file
- prioritize high-signal evidence such as README files, core code, configs, deployment files, APIs, data flows, and architecture clues
- dynamically adjust emphasis according to target role or JD
- output one final resume-ready version instead of multiple redundant versions
- enforce evidence-first writing and avoid inflated claims
- extract a dedicated tech stack line using role-aware priority rules

## Output Shape

The expected output contains:

- a short evidence analysis
- one final resume-ready project description
- a dedicated tech stack line when the repository supports explicit stack extraction

The writing style is optimized for real resumes rather than long project introductions.

## Repository Layout

```text
repo-to-resume-tailor/
|- README.md
|- LICENSE
|- .gitignore
|- repo-to-resume-tailor/
|  |- SKILL.md
|  |- role_mapping.md
|  |- agents/
|  |  |- openai.yaml
|  |- references/
|     |- prompt.md
|     |- examples.md
|- examples/
|  |- personal-role-case.md
|  |- personal-jd-case.md
|- docs/
   |- codex.md
   |- claude-code.md
   |- cursor.md
```

## Key Components

- `repo-to-resume-tailor/SKILL.md`
  Core execution rules and output contract
- `repo-to-resume-tailor/role_mapping.md`
  Role capability mapping and stack-priority templates
- `repo-to-resume-tailor/references/prompt.md`
  Reusable long-form prompt reference
- `examples/`
  Realistic role-mode and JD-mode examples
- `docs/`
  Notes for using the package across different AI coding tools

## Installation and Usage

### Codex

Copy the inner `repo-to-resume-tailor/` folder into your Codex skills directory so the installed layout becomes:

```text
~/.codex/skills/repo-to-resume-tailor/
  SKILL.md
  role_mapping.md
  agents/openai.yaml
  references/prompt.md
  references/examples.md
```

See [docs/codex.md](docs/codex.md).

### Claude Code

Claude Code does not use the same native skill format. Reuse `SKILL.md`, `role_mapping.md`, and `references/prompt.md` as a reusable project prompt or instruction set.

See [docs/claude-code.md](docs/claude-code.md).

### Cursor

Cursor can reuse this package as a project rule, reusable prompt, or agent instruction set.

See [docs/cursor.md](docs/cursor.md).

## Quick Start

Example prompt for target-role mode:

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description tailored to an AI / Agent development role.
```

Example prompt for JD mode:

```text
Use $repo-to-resume-tailor to analyze this repository and rewrite the project experience for the following job description: ...
```

## Examples

- target role example: [examples/personal-role-case.md](examples/personal-role-case.md)
- specific JD example: [examples/personal-jd-case.md](examples/personal-jd-case.md)

## License

MIT License. See [LICENSE](LICENSE).

---

## 中文说明

`repo-to-resume-tailor` 是一个通用的 skill / prompt 规则包，用来把代码仓库转换成适合写入简历的项目描述。它会基于仓库中的真实证据分析项目内容，再根据目标岗位方向或具体岗位 JD，生成简洁、可信、贴近招聘筛选逻辑的项目经历文本，而不是泛泛的仓库总结。

## 项目定位

这个项目主要面向两类使用场景：

- 目标岗位模式：用户只提供岗位方向，例如后端、前端、AI / Agent、数据、全栈、DevOps、安全等
- JD 模式：用户直接粘贴某个公司的具体岗位 JD，希望按该 JD 改写项目描述

这个仓库是平台中立的：

- 在 Codex 中可以作为原生 skill 使用
- 在 Claude Code、Cursor 或其他类似工具中，也可以作为提示词和规则包复用

## 核心能力

- 分析整个仓库，而不是只看单个文件
- 优先读取高信号证据，例如 README、核心代码、配置文件、部署文件、API、数据流和架构说明
- 根据岗位方向或 JD 动态调整提炼重点
- 只输出一个最终简历版本，不输出冗余的多版本结果
- 强制遵循证据优先原则，避免夸大或虚构
- 按岗位优先级提取独立的技术栈一行

## 输出形式

最终输出通常包括：

- 一段简短分析，说明主要证据来源、匹配岗位能力、哪些表述需要保守
- 一版最终简历项目描述
- 一行单独的技术栈总结

整体风格偏向真实简历，而不是长篇项目介绍。

## 目录结构

```text
repo-to-resume-tailor/
|- README.md
|- LICENSE
|- .gitignore
|- repo-to-resume-tailor/
|  |- SKILL.md
|  |- role_mapping.md
|  |- agents/
|  |  |- openai.yaml
|  |- references/
|     |- prompt.md
|     |- examples.md
|- examples/
|  |- personal-role-case.md
|  |- personal-jd-case.md
|- docs/
   |- codex.md
   |- claude-code.md
   |- cursor.md
```

## 关键文件

- `repo-to-resume-tailor/SKILL.md`
  核心执行规则与输出约束
- `repo-to-resume-tailor/role_mapping.md`
  岗位能力映射与技术栈优先级模板
- `repo-to-resume-tailor/references/prompt.md`
  可复用的长提示词模板
- `examples/`
  真实的岗位模式与 JD 模式示例
- `docs/`
  不同 AI coding 工具下的使用说明

## 安装与使用

### Codex

把内部的 `repo-to-resume-tailor/` 目录复制到 Codex 的 skills 目录中，使安装后的结构变成：

```text
~/.codex/skills/repo-to-resume-tailor/
  SKILL.md
  role_mapping.md
  agents/openai.yaml
  references/prompt.md
  references/examples.md
```

详见 [docs/codex.md](docs/codex.md)。

### Claude Code

Claude Code 不使用完全相同的原生 skill 格式，但可以把 `SKILL.md`、`role_mapping.md` 和 `references/prompt.md` 当作可复用规则集来使用。

详见 [docs/claude-code.md](docs/claude-code.md)。

### Cursor

Cursor 可以把这套内容作为 project rule、reusable prompt 或 agent instruction 使用。

详见 [docs/cursor.md](docs/cursor.md)。

## 快速开始

目标岗位模式示例：

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description tailored to an AI / Agent development role.
```

JD 模式示例：

```text
Use $repo-to-resume-tailor to analyze this repository and rewrite the project experience for the following job description: ...
```

## 示例

- 岗位方向示例：[examples/personal-role-case.md](examples/personal-role-case.md)
- 具体 JD 示例：[examples/personal-jd-case.md](examples/personal-jd-case.md)

## License

采用 MIT License，详见 [LICENSE](LICENSE)。
