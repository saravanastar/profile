# Repository Agent Guide

This repository contains a resume generator and JSON resume datasets for multiple profiles.

## Project purpose
- Generate resumes from JSON files using the Python script in src/generate_profile.py.
- Keep resume content concise, tailored, and aligned to the target role.
- Prefer updating existing JSON structure rather than inventing a new one.

## Core files
- Makefile: entry points for generating resumes.
- src/generate_profile.py: script that converts JSON resume data into a DOCX/PDF resume.
- src/data/*.json: resume source datasets.

## When editing resume content
- Preserve the existing JSON shape: name, contact, social, other, profileSummary, skills, certifications, projects, experiences, education.
- Keep bullet points achievement-focused and measurable where possible.
- Tailor the summary, skills, and experience bullets to the target company or role.
- For new variants, mirror the structure from existing files such as ask_long.json or ask_infra.json.

## Common commands
- make ask
- make long
- make short
- make poorni
- make infra

## Rules for agents
- Do not change the generator logic unless the task explicitly requires it.
- Do not invent credentials, fake metrics, or unverifiable achievements.
- Keep language professional and resume-ready.
- If a new resume variant is requested, add a new JSON file in src/data/ and keep it consistent with the existing schema.
