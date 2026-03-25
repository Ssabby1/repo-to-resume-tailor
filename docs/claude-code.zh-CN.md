# Claude Code 安装说明

## 推荐方式

全局安装：

```bash
pip install .
repo-to-resume-tailor init --ai claude-code
```

项目级安装：

```bash
repo-to-resume-tailor init --ai claude-code --scope project --project /path/to/your/project
```

备用方式：

```bash
python install.py --ai claude-code
python install.py --ai claude-code --scope project --project /path/to/your/project
```

安装器会生成一个 slash command 文件：

```text
~/.claude/commands/repo-to-resume-tailor.md
```

如果是项目级安装，则生成到：

```text
/path/to/your/project/.claude/commands/repo-to-resume-tailor.md
```

## 使用方式

示例：

```text
/repo-to-resume-tailor AI / Agent Development
```

这个命令会复用与 Codex skill 相同的证据优先、岗位映射和防过度包装规则。
