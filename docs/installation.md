# Installation

This repository now includes an installable Python CLI so you do not need to manually copy files into each tool's configuration directory.

## Recommended Flow

From the repository root:

```bash
pip install .
```

Then use:

```bash
repo-to-resume-tailor init --ai codex
```

If you do not want to install the package yet, you can still run the bundled compatibility script:

```bash
python install.py --ai codex
```

## Fallback Method

If `pip install .` fails because of local Python, pip, permission, or environment issues, use the repository-bundled installer directly:

```bash
python install.py --ai codex
python install.py --ai claude-code
python install.py --ai cursor --project /path/to/your/project
```

This fallback does not require the CLI package to be installed globally. It runs directly from the cloned repository and is the safest backup path for new machines.

## AI-Assisted Install

You can also ask your coding agent to install the package directly from GitHub:

```text
Install this package from https://github.com/Ssabby1/repo-to-resume-tailor and set it up for Codex.
```

```text
Install this package from https://github.com/Ssabby1/repo-to-resume-tailor and configure it for Claude Code.
```

```text
Install this package from https://github.com/Ssabby1/repo-to-resume-tailor and add it to my current Cursor project.
```

This approach works best when the agent can access GitHub, run shell commands, and write to the relevant tool configuration directories.

## Quick Commands

### Codex

```bash
repo-to-resume-tailor init --ai codex
```

This installs the inner skill folder into:

```text
~/.codex/skills/repo-to-resume-tailor/
```

### Claude Code

Global command install:

```bash
repo-to-resume-tailor init --ai claude-code
```

Project command install:

```bash
repo-to-resume-tailor init --ai claude-code --scope project --project /path/to/your/project
```

This creates a slash command file named:

```text
~/.claude/commands/repo-to-resume-tailor.md
```

or, for project scope:

```text
/path/to/your/project/.claude/commands/repo-to-resume-tailor.md
```

You can then call:

```text
/repo-to-resume-tailor AI / Agent Development
```

### Cursor

Cursor rules are project-scoped, so install into a target project:

```bash
repo-to-resume-tailor init --ai cursor --project /path/to/your/project
```

This creates:

```text
/path/to/your/project/.cursor/rules/repo-to-resume-tailor.mdc
```

## Notes

- Codex installation copies the native skill package
- Claude Code installation generates a reusable slash command
- Cursor installation generates a project rule file
- Cursor uses project rules rather than a single global skill folder
- `python install.py ...` remains available as a compatibility wrapper around the CLI
- For maximum compatibility on a new machine, the repository installer is the official fallback
