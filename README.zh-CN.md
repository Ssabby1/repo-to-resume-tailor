# repo-to-resume-tailor

[English](README.md)

`repo-to-resume-tailor` 是一个通用的 skill / prompt 规则包，用来把代码仓库转换成适合写入简历的项目描述。它会基于仓库中的真实证据分析项目内容，再根据目标岗位方向或具体岗位 JD，生成简洁、可信、贴近招聘筛选逻辑的项目经历文本，而不是泛泛的仓库总结。

## 项目定位

这个项目主要面向两类使用场景：

- 目标岗位模式：用户只提供岗位方向，例如后端、前端、AI / Agent、数据、全栈、DevOps、安全等
- JD 模式：用户直接粘贴某个公司的具体岗位 JD，希望按该 JD 改写项目描述

这个仓库是平台中立的：

- 在 Codex 中可以作为原生 skill 使用
- 在 Claude Code、Cursor 或其他类似工具中，也可以通过生成命令或规则文件来复用

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
|- README.zh-CN.md
|- LICENSE
|- .gitignore
|- pyproject.toml
|- install.py
|- src/
|  |- repo_to_resume_tailor_cli/
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
|  |- personal-role-case.zh-CN.md
|  |- personal-jd-case.md
|  |- personal-jd-case.zh-CN.md
|- docs/
   |- installation.md
   |- installation.zh-CN.md
   |- codex.md
   |- codex.zh-CN.md
   |- claude-code.md
   |- claude-code.zh-CN.md
   |- cursor.md
   |- cursor.zh-CN.md
```

## 关键文件

- `repo-to-resume-tailor/SKILL.md`
  核心执行规则与输出约束
- `repo-to-resume-tailor/role_mapping.md`
  岗位能力映射与技术栈优先级模板
- `repo-to-resume-tailor/references/prompt.md`
  可复用的长提示词模板
- `src/repo_to_resume_tailor_cli/`
  面向 Codex、Claude Code、Cursor 的可安装 CLI
- `examples/`
  真实的岗位模式与 JD 模式示例，包含中英文版本
- `docs/`
  不同 AI coding 工具下的安装和使用说明

## 安装与使用

推荐方式：

```bash
pip install .
repo-to-resume-tailor init --ai codex
repo-to-resume-tailor init --ai claude-code
repo-to-resume-tailor init --ai cursor --project /path/to/your/project
```

如果 CLI 安装失败，可使用备用方式：

```bash
python install.py --ai codex
python install.py --ai claude-code
python install.py --ai cursor --project /path/to/your/project
```

也支持让 AI coding agent 直接代装。你可以直接对自己的工具说：

```text
帮我从 https://github.com/Ssabby1/repo-to-resume-tailor 安装这个仓库，并按 Codex 方式部署。
```

```text
帮我从 https://github.com/Ssabby1/repo-to-resume-tailor 安装这个仓库，并配置到 Claude Code。
```

```text
帮我从 https://github.com/Ssabby1/repo-to-resume-tailor 安装这个仓库，并配置到我当前的 Cursor 项目里。
```

安装细节请看：

- [English installation guide](docs/installation.md)
- [中文安装说明](docs/installation.zh-CN.md)

工具专属说明：

- [Codex](docs/codex.md) | [中文](docs/codex.zh-CN.md)
- [Claude Code](docs/claude-code.md) | [中文](docs/claude-code.zh-CN.md)
- [Cursor](docs/cursor.md) | [中文](docs/cursor.zh-CN.md)

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

- 岗位方向示例：[英文版](examples/personal-role-case.md) / [中文版](examples/personal-role-case.zh-CN.md)
- 具体 JD 示例：[英文版](examples/personal-jd-case.md) / [中文版](examples/personal-jd-case.zh-CN.md)

## 社区

[linux.do](https://linux.do/)

## License

采用 MIT License，详见 [LICENSE](LICENSE)。
