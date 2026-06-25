# Copilot Instructions for this repository

This repo contains a resume generator and several JSON resume datasets.

## Workflow
- Use the existing JSON schema when updating or creating resume content.
- Prefer editing the relevant JSON file in src/data before generating a resume.
- Generate output with the Makefile targets or the Python script.

## Supported resume generation commands
- make ask
- make long
- make short
- make poorni
- make infra

## Resume content guidance
- Keep content concise and tailored to the target role.
- Prefer outcomes, impact, and measurable results.
- For AI infrastructure roles, emphasize Kubernetes, platform engineering, observability, SRE, RAG, LLM inference, and model serving.
- For new variants, preserve the structure from the existing JSON files.
