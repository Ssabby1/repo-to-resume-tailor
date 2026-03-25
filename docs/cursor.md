# Cursor Installation

## Recommended

Cursor rules are project-scoped, so install into a target project:

```bash
pip install .
repo-to-resume-tailor init --ai cursor --project /path/to/your/project
```

Fallback:

```bash
python install.py --ai cursor --project /path/to/your/project
```

This generates:

```text
/path/to/your/project/.cursor/rules/repo-to-resume-tailor.mdc
```

## Usage

After installation, open the target project in Cursor and invoke the agent with a prompt such as:

```text
Analyze this repository and write one resume-ready project description based only on repository evidence, tailored to the following role or JD, with a dedicated tech stack line.
```

The generated rule keeps the repository-analysis and anti-exaggeration constraints aligned with the main skill package.
