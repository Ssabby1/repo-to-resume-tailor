# repo-to-resume-tailor

`repo-to-resume-tailor` is a Codex-first skill package for turning a source code repository into one resume-ready project description. It analyzes repository evidence, ranks project details by target role or job description, and produces concise, credible project experience text instead of generic summaries.

## What It Does

- Analyze a full repository instead of a single file
- Prioritize high-signal evidence such as README files, core code, configs, deployment files, APIs, data flows, and architecture clues
- Tailor output to backend, AI or agent, data, full-stack, platform, or MLOps roles
- Support a concrete job description as the primary matching signal
- Enforce evidence-first writing and avoid over-claiming

## Output Shape

The skill asks Codex to produce:

- a short evidence summary
- one final resume-ready version tailored to the user's input
- a dedicated tech stack line when the repository supports explicit stack extraction

It is optimized for short resume wording rather than long project introductions.

## Input Modes

The skill supports exactly two input modes:

- target-role mode: the user provides a target role direction such as backend, AI or agent, or data
- JD mode: the user pastes a concrete company job description

The skill should output only one version, chosen according to the input mode.

## Role Mapping

The skill uses a dedicated role mapping reference at [role_mapping.md](C:\Users\sasa\Documents\Playground\repo-to-resume-tailor\repo-to-resume-tailor\role_mapping.md).

This reference covers backend, frontend, full-stack, mobile, testing, DevOps, data, analysis, algorithm, AI or LLM or agent, recommendation, desktop client, security, game, technical product, and technical project management scenarios.

If a role title is not explicitly covered, the skill should map it to the nearest category by underlying responsibilities instead of literal title matching.

## Key Guardrails

- Use evidence priority instead of surface-level stack matching
- Keep output short enough for resumes
- Prefer conservative wording when evidence is incomplete
- Do not invent metrics, impact, ownership, or unsupported architecture claims
- Do not describe third-party API integration as self-developed model capability

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

## Install

### Codex

Copy the inner skill folder into your Codex skills directory so the final layout becomes:

```text
~/.codex/skills/repo-to-resume-tailor/
  SKILL.md
  role_mapping.md
  agents/openai.yaml
  references/prompt.md
  references/examples.md
```

Detailed steps are in [docs/codex.md](C:\Users\sasa\Documents\Playground\repo-to-resume-tailor\docs\codex.md).

### Claude Code

Claude Code does not use the same native skill format. Reuse the rules in `SKILL.md`, `role_mapping.md`, and `references/prompt.md` as a reusable instruction or project prompt.

See [docs/claude-code.md](C:\Users\sasa\Documents\Playground\repo-to-resume-tailor\docs\claude-code.md).

### Cursor

Cursor can reuse the prompt and rules as a project rule, reusable prompt, or agent instruction.

See [docs/cursor.md](C:\Users\sasa\Documents\Playground\repo-to-resume-tailor\docs\cursor.md).

## Quick Start

Example prompt for target-role mode:

```text
Use $repo-to-resume-tailor to analyze this repository and write one resume-ready project description tailored to an AI / Agent development role.
```

Example prompt for JD mode:

```text
Use $repo-to-resume-tailor to analyze this repository and rewrite the project experience for the following JD: ...
```

## Examples

- Target role example: [examples/personal-role-case.md](C:\Users\sasa\Documents\Playground\repo-to-resume-tailor\examples\personal-role-case.md)
- Specific JD example: [examples/personal-jd-case.md](C:\Users\sasa\Documents\Playground\repo-to-resume-tailor\examples\personal-jd-case.md)

## License

This repository currently uses the MIT License.
