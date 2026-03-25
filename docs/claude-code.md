# Claude Code Installation

## Recommended

Global install:

```bash
pip install .
repo-to-resume-tailor init --ai claude-code
```

Project-scoped install:

```bash
repo-to-resume-tailor init --ai claude-code --scope project --project /path/to/your/project
```

Fallback:

```bash
python install.py --ai claude-code
python install.py --ai claude-code --scope project --project /path/to/your/project
```

The installer generates a slash command file:

```text
~/.claude/commands/repo-to-resume-tailor.md
```

or, for project scope:

```text
/path/to/your/project/.claude/commands/repo-to-resume-tailor.md
```

## Usage

Example:

```text
/repo-to-resume-tailor AI / Agent Development
```

The generated command reuses the same evidence-first, role-aware rules as the native Codex skill.
