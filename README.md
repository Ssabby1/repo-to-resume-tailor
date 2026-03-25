# repo-to-resume-tailor

[中文说明](README.zh-CN.md)

`repo-to-resume-tailor` is a reusable skill and prompt package for turning a source code repository into a resume-ready project description. It analyzes repository evidence, matches the project against a target role or a specific job description, and produces concise, credible, hiring-oriented project text instead of a generic repository summary.

## Overview

This project is designed for two common resume-writing scenarios:

- target-role mode: the user provides a target role direction such as backend, frontend, AI or agent, data, full-stack, DevOps, or security
- JD mode: the user pastes a concrete job description and wants the project description tailored to it

The package is platform-friendly rather than platform-exclusive:

- on Codex, it can be used as a native skill
- on Claude Code, Cursor, or similar tools, it can be reused through generated commands or rules

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

## Key Components

- `repo-to-resume-tailor/SKILL.md`
  Core execution rules and output contract
- `repo-to-resume-tailor/role_mapping.md`
  Role capability mapping and stack-priority templates
- `repo-to-resume-tailor/references/prompt.md`
  Reusable long-form prompt reference
- `src/repo_to_resume_tailor_cli/`
  Installable CLI for Codex, Claude Code, and Cursor
- `examples/`
  Realistic role-mode and JD-mode examples in English and Chinese
- `docs/`
  Usage notes and installation references for different AI coding tools

## Installation and Usage

Recommended:

```bash
pip install .
repo-to-resume-tailor init --ai codex
repo-to-resume-tailor init --ai claude-code
repo-to-resume-tailor init --ai cursor --project /path/to/your/project
```

Fallback if CLI installation fails:

```bash
python install.py --ai codex
python install.py --ai claude-code
python install.py --ai cursor --project /path/to/your/project
```

Detailed installation notes:

- [English installation guide](docs/installation.md)
- [中文安装说明](docs/installation.zh-CN.md)

Tool-specific references:

- [Codex](docs/codex.md) | [中文](docs/codex.zh-CN.md)
- [Claude Code](docs/claude-code.md) | [中文](docs/claude-code.zh-CN.md)
- [Cursor](docs/cursor.md) | [中文](docs/cursor.zh-CN.md)

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

- target role example: [English](examples/personal-role-case.md) | [中文](examples/personal-role-case.zh-CN.md)
- specific JD example: [English](examples/personal-jd-case.md) | [中文](examples/personal-jd-case.zh-CN.md)

## Community

[linux.do](https://linux.do/)

## License

MIT License. See [LICENSE](LICENSE).
