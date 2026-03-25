from __future__ import annotations

import argparse
import importlib.resources as resources
import shutil
import sys
from pathlib import Path


SKILL_NAME = "repo-to-resume-tailor"
PACKAGE_ROOT = Path(__file__).resolve().parents[2]
DEV_SKILL_DIR = PACKAGE_ROOT / SKILL_NAME


def get_skill_dir() -> Path:
    if DEV_SKILL_DIR.exists():
        return DEV_SKILL_DIR
    return Path(resources.files("repo_to_resume_tailor_cli")) / "data" / SKILL_NAME


SKILL_DIR = get_skill_dir()
PROMPT_FILE = SKILL_DIR / "references" / "prompt.md"
ROLE_MAPPING_FILE = SKILL_DIR / "role_mapping.md"


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def install_codex() -> Path:
    target_root = Path.home() / ".codex" / "skills"
    target_root.mkdir(parents=True, exist_ok=True)
    target = target_root / SKILL_NAME
    copy_tree(SKILL_DIR, target)
    return target


def build_claude_command() -> str:
    prompt_text = read_text(PROMPT_FILE).strip()
    role_mapping_text = read_text(ROLE_MAPPING_FILE).strip()
    return f"""---
description: Turn a code repository into one resume-ready project description tailored to a target role or specific job description
---

# Repo to Resume Tailor

Use this command to analyze the current repository and write one resume-ready project description.

Behavior requirements:
- Base every claim on repository evidence
- If the user gives a target role direction, tailor to that role
- If the user gives a specific job description, prioritize repeated JD responsibilities, keywords, and delivery expectations
- Output a short evidence analysis first
- Then output one final resume-ready version only
- Include a dedicated tech stack line when supported by repository evidence
- Do not fabricate metrics, unsupported ownership, or imaginary outcomes

Use any arguments passed to this slash command as the user's target role or job description. If arguments are missing, ask the user to provide either a target role direction or a concrete job description.

## Core Prompt Reference

{prompt_text}

## Role Mapping Reference

{role_mapping_text}
"""


def install_claude_code(scope: str, project: str | None) -> Path:
    if scope == "global":
        commands_dir = Path.home() / ".claude" / "commands"
    else:
        if not project:
            raise ValueError("--project is required when --scope project is used for claude-code")
        commands_dir = Path(project).expanduser().resolve() / ".claude" / "commands"
    commands_dir.mkdir(parents=True, exist_ok=True)
    target = commands_dir / f"{SKILL_NAME}.md"
    target.write_text(build_claude_command(), encoding="utf-8")
    return target


def build_cursor_rule() -> str:
    prompt_text = read_text(PROMPT_FILE).strip()
    return f"""---
description: Turn a repository into one resume-ready project description tailored to a target role or specific job description
globs:
alwaysApply: false
---

# Repo to Resume Tailor

Use this rule when the user wants to:
- turn a repository into a resume-ready project description
- tailor project wording to a target role
- tailor project wording to a specific job description

Requirements:
- analyze repository evidence before writing
- prioritize README files, docs, core business code, config, deployment, APIs, data flow, and tests
- output one final resume-ready version only
- include a dedicated tech stack line when explicitly supported
- do not fabricate metrics, unsupported ownership, or imaginary outcomes
- when a JD is provided, prioritize repeated JD responsibilities and technical keywords

Reference:

{prompt_text}
"""


def install_cursor(project: str | None) -> Path:
    if not project:
        raise ValueError("--project is required for cursor because Cursor project rules live inside the target project")
    rules_dir = Path(project).expanduser().resolve() / ".cursor" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    target = rules_dir / f"{SKILL_NAME}.mdc"
    target.write_text(build_cursor_rule(), encoding="utf-8")
    return target


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install repo-to-resume-tailor for Codex, Claude Code, or Cursor."
    )
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Install repo-to-resume-tailor into a target AI tool")
    init_parser.add_argument("--ai", required=True, choices=["codex", "claude-code", "cursor"])
    init_parser.add_argument(
        "--scope",
        choices=["global", "project"],
        default=None,
        help="Install scope. Codex uses global. Claude Code supports global or project. Cursor uses project.",
    )
    init_parser.add_argument(
        "--project",
        help="Target project path for project-scoped installs. Required for Cursor and Claude Code project installs.",
    )

    return parser


def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    try:
        if args.ai == "codex":
            target = install_codex()
            print(f"[OK] Installed {SKILL_NAME} for Codex at:")
            print(target)
            print(f"Use it with: {SKILL_NAME} or ${SKILL_NAME}")
            return 0

        if args.ai == "claude-code":
            scope = args.scope or "global"
            target = install_claude_code(scope=scope, project=args.project)
            print(f"[OK] Installed {SKILL_NAME} for Claude Code ({scope}) at:")
            print(target)
            print(f"Use it with: /{SKILL_NAME} <target role or JD>")
            return 0

        if args.ai == "cursor":
            target = install_cursor(project=args.project)
            print(f"[OK] Installed {SKILL_NAME} for Cursor project rules at:")
            print(target)
            print("Open the target project in Cursor and invoke the rule from Agent context.")
            return 0

    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    print("[ERROR] Unsupported install target.", file=sys.stderr)
    return 1
