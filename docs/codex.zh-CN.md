# Codex 安装说明

## 推荐方式

在仓库根目录执行：

```bash
pip install .
repo-to-resume-tailor init --ai codex
```

如果暂时不想安装 CLI，也可以使用备用脚本：

```bash
python install.py --ai codex
```

这会把原生 skill 安装到：

```text
~/.codex/skills/repo-to-resume-tailor/
```

安装后的结构应包含：

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

你也可以直接提供具体岗位 JD，让它按 JD 重写项目经历。
