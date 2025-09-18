# 01_web_app/backend Agent Guide

## Purpose
Coordinate backend behaviour for the document management web app.

## Current Layout
- `../app.py`: Flask app factory with the current routes (`/`, `/upload`, `/error`) and error handlers.
- `../services/file_service.py`: validation and persistence logic for uploads.
- `../exceptions.py`: shared exception definitions.
- `backend/`: reserved space for modular blueprints (`routes/`, `services/`, etc.) as the app grows.

## Responsibilities
- Keep `app.py` lean by moving complex logic into dedicated modules under `backend/` or `../services/`.
- Introduce blueprints under `backend/routes/` once a feature needs its own module.
- Share reusable helpers under `../services/` to avoid duplication.
- Update backend documentation (`AGENTS.md`, `README.md`) whenever structure changes.

## Contribution Workflow
1. Design the API surface for the feature (new route or blueprint).
2. Implement request handling in `app.py` or a blueprint under `backend/routes/`.
3. Add supporting business logic in `../services/` and custom errors in `../exceptions.py` if required.
4. Extend tests in `tests/` to cover the behaviour.
5. Run `pytest` and update docs as needed.

## Quality Checklist
- Run `pytest` from the project root.
- Format Python files with `black`.
- Lint Markdown updates with `npx markdownlint README.md`.
- Ensure uploads created during tests are cleaned up.

## Notes
This directory is intentionally light today; expand it organically as features demand more structure.
