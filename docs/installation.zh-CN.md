# 安装说明

这个仓库现在自带了一个可安装的 Python CLI，不需要再手动把文件复制到各个工具的配置目录。

## 推荐安装流程

在仓库根目录执行：

```bash
pip install .
```

安装后直接使用：

```bash
repo-to-resume-tailor init --ai codex
```

如果你暂时不想安装成系统命令，也可以继续使用仓库里的兼容脚本：

```bash
python install.py --ai codex
```

## 备用安装方式

如果 `pip install .` 因为本地 Python、pip、权限或环境差异失败，直接使用仓库自带的安装脚本：

```bash
python install.py --ai codex
python install.py --ai claude-code
python install.py --ai cursor --project /path/to/your/project
```

这个备用方案不依赖全局 CLI 安装，直接在 clone 下来的仓库里运行，是新电脑上最稳妥的兜底方式。

## 让 AI 代理代装

你也可以直接让自己的 AI coding agent 从 GitHub 安装：

```text
帮我从 https://github.com/Ssabby1/repo-to-resume-tailor 安装这个仓库，并按 Codex 方式部署。
```

```text
帮我从 https://github.com/Ssabby1/repo-to-resume-tailor 安装这个仓库，并配置到 Claude Code。
```

```text
帮我从 https://github.com/Ssabby1/repo-to-resume-tailor 安装这个仓库，并配置到我当前的 Cursor 项目里。
```

这种方式更适合已经在使用 Codex、Claude Code、Cursor 等代理工具，并且代理具备 GitHub 访问、命令执行和本地写入权限的场景。

## 快速安装命令

### Codex

```bash
repo-to-resume-tailor init --ai codex
```

这会把 skill 安装到：

```text
~/.codex/skills/repo-to-resume-tailor/
```

### Claude Code

全局命令安装：

```bash
repo-to-resume-tailor init --ai claude-code
```

项目级命令安装：

```bash
repo-to-resume-tailor init --ai claude-code --scope project --project /path/to/your/project
```

这会生成一个 slash command 文件：

```text
~/.claude/commands/repo-to-resume-tailor.md
```

如果是项目级安装，则生成到：

```text
/path/to/your/project/.claude/commands/repo-to-resume-tailor.md
```

之后你可以直接调用：

```text
/repo-to-resume-tailor AI / Agent Development
```

### Cursor

Cursor 的规则是项目级的，所以需要指定目标项目路径：

```bash
repo-to-resume-tailor init --ai cursor --project /path/to/your/project
```

这会生成：

```text
/path/to/your/project/.cursor/rules/repo-to-resume-tailor.mdc
```

## 说明

- Codex：安装原生 skill 包
- Claude Code：生成可直接调用的 slash command
- Cursor：生成项目规则文件
- Cursor 本身更适合 project rule 形式，而不是单独的全局 skill 目录
- `python install.py ...` 依然保留，可作为 CLI 的兼容入口
- 对于全新电脑，仓库自带安装脚本是官方兜底方案
