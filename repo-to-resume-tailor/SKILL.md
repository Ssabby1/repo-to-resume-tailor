---
name: repo-to-resume-tailor
description: Analyze a full code repository and generate one resume-ready project description grounded in repository evidence. Use when Codex is asked to turn a repository into concise project bullets, project summaries, or tailored experience based on either a target role direction or a specific job description for backend, AI or agent, AI product, data, full-stack, platform, or MLOps roles.
---

# Repo to Resume Tailor

## Overview

Analyze the repository before writing. Extract only verifiable project facts, then rewrite them into concise, resume-appropriate project descriptions. Optimize for credibility, role relevance, and hiring readability instead of broad repository summarization.

Dynamically adjust extraction and writing priorities based on the user's target role direction or specific job description. For AI or Agent or LLM, AI product, backend, frontend, full-stack, data, algorithm, DevOps, security, testing, and related roles, prioritize the most role-relevant implementation evidence and technical proof from the repository. If a concrete job description is provided, treat its frequent responsibilities, technical keywords, and delivery expectations as the highest priority. If the role name is not directly covered, map it to the nearest role category based on the underlying responsibilities. Do not invent technologies, responsibilities, or outcomes that are not supported by repository evidence in order to improve match quality.

Adjust repository analysis and project phrasing dynamically according to the user's target role direction or specific job description. Do not mechanically list every technology in the repository. Instead, prioritize the abilities, modules, and implementation details that are most relevant to the target role. If the user provides a concrete job description, treat its high-frequency responsibilities, keywords, and technical requirements as the highest priority.

## Workflow

1. Clarify the input mode.
   Use one of these two modes:
   - target-role mode: the user gives a role direction such as backend, AI or agent, data, full-stack, platform, or MLOps
   - JD mode: the user pastes a concrete company job description
   In target-role mode, prioritize the capability mapping for that role.
   In JD mode, prioritize the keywords, skills, and responsibilities from the job description.
2. Traverse the repository selectively and prioritize high-signal evidence.
3. Ignore low-value noise aggressively.
4. Build an evidence-backed view of project positioning, tech stack, modules, and delivery form.
5. Rank findings by role fit, not by broad coverage.
6. Write with evidence discipline and conservative wording where needed.

## Evidence Priority

- Level 1 evidence: README, architecture or design docs, code comments with intent, API definitions, config files, deployment files, schema definitions
- Level 2 evidence: directory structure, module naming, dependency inference, service boundaries implied by code organization
- Level 3 evidence: reasonable inference from surrounding code

If a claim depends mostly on Level 3 evidence, weaken the wording instead of presenting it as a confirmed fact.

## Role Mapping

Use the role mapping reference in [role_mapping.md](role_mapping.md) when matching repository evidence to role categories.

- When the role is directly covered, prioritize the mapped capability areas and evidence patterns from that reference.
- When the user provides a concrete job description, use the role mapping as a helper but let repeated job-description responsibilities, keywords, and delivery requirements take highest priority.
- When the role is not directly covered, merge it into the nearest category by underlying responsibilities rather than by title wording.
- For AI product roles, prioritize product problem definition, user scenarios, feature structure, capability boundaries, evaluation loops, and landing strategy over raw infrastructure details. Even if the repository uses RAG, prompts, agent workflows, or orchestration frameworks, explain how those capabilities serve product goals and user experience.
- If the repository mainly proves technical implementation but lacks clear product documents, workflow design, evaluation loops, or productized evidence, do not over-package it as an AI product project.
- Never increase match quality by inventing unsupported technologies, responsibilities, or outcomes.

## Tech Stack Extraction

Always extract and output a dedicated tech stack line when the repository supports it.

- Prefer explicit technology names proven by code, config, imports, dependencies, framework usage, or workflow files
- For AI or agent projects, explicitly surface technologies such as RAG, LangGraph, FastAPI, vector databases, embedding pipelines, tool calling, workflow orchestration, and model SDKs when the repository supports them
- Do not hide the stack only inside prose when it can be named directly
- Do not guess stack items that are not evidenced
- Use the tech stack priority templates in [role_mapping.md](role_mapping.md) to decide stack ordering, grouping, and maximum stack count for high-frequency role categories

## Writing Rules

- Base every final statement on repository evidence
- Do not fabricate metrics, impact, scale, ownership scope, or unsupported architecture claims
- Do not describe a course assignment as a production system
- Do not describe a forked project as fully self-built unless the repository supports that
- Do not describe third-party API integration as self-developed model capability
- Do not assign the user an unverified role such as project owner, system architect, or primary lead

Prefer conservative wording when evidence is incomplete, such as:
- participated in implementing
- implemented a basic capability for
- the project includes
- the repository structure suggests the focus is

## Output Contract

Before the resume text, output a short analysis section covering:
- which file types or directories were used as the main evidence
- which role capabilities the project best matches
- which claims are strongly supported and which ones remain conservative

Then output one final resume-ready version only.

The final output should include:
- project name
- project positioning or background
- tech stack summary on its own line
- core implementation, modules, or technical highlights
- outcomes only when clearly supported by repository evidence

Keep the output short enough for a real resume:
- about 90 to 150 Chinese characters for the main project summary, or
- 3 to 4 bullet points, each about 20 to 35 Chinese characters

Do not output two versions in the same response.
Select the one version that best matches the user's input mode:
- if the user gives only a target role, output one version tailored to that role
- if the user gives a concrete job description, output one version tailored to that job description

## References

Read [references/prompt.md](references/prompt.md) when the user wants a fuller reusable prompt template or stricter output language.

Read [references/examples.md](references/examples.md) when you need concrete examples of evidence handling and output shaping.

Read [role_mapping.md](role_mapping.md) when selecting which repository signals matter most for a target role or job description.
