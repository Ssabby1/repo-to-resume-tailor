# Claude Code Adaptation

Claude Code does not use the same native skill packaging as Codex. Reuse the content in:

- `repo-to-resume-tailor/SKILL.md`
- `repo-to-resume-tailor/references/prompt.md`

Recommended approaches:

- place the rules into a reusable prompt template
- store the long prompt in a project note or command snippet
- keep the evidence-first and anti-exaggeration rules unchanged

Suggested adaptation prompt:

```text
Analyze this repository and turn it into one resume-ready project description. Base every claim on repository evidence, rank details by target role or JD fit, output a short evidence analysis first, include a dedicated tech stack line, and do not invent metrics or unsupported ownership claims.
```
