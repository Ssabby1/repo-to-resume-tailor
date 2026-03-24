# Cursor Adaptation

Cursor can reuse this project as a ruleset rather than a native Codex skill.

Recommended approaches:

- copy `repo-to-resume-tailor/SKILL.md` into a project rule or agent rule
- use `repo-to-resume-tailor/references/prompt.md` as a reusable long prompt
- keep examples in `examples/` for testing prompt quality

Suggested usage:

```text
Analyze this repository and write one resume-ready project description based only on repository evidence, tailored to the following role or JD, with a dedicated tech stack line.
```
