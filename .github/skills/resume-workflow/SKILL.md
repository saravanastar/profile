---
name: resume-workflow
description: "Use when updating resume content, creating a new resume variant, or generating a resume from the repository."
---

# Resume Workflow

Use this skill when you need to update resume data or generate a new resume from the repository.

## Steps
1. Review the existing resume JSON in src/data and match the current structure.
2. Update the relevant fields for the target role or company.
3. Generate the resume using the Makefile target or the Python script.
4. Keep the tone concise, measurable, and tailored.

## Important notes
- Preserve the JSON schema.
- Avoid inventing unsupported facts.
- Prefer role-specific wording for AI infrastructure, platform, or SRE positions.
- Common generation commands: make ask, make long, make short, make poorni, make infra.
