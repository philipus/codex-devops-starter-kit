# Test Guide

## Purpose
This folder contains automated tests that verify the Flask file-upload application remains stable.

## Scope
- Integration-style tests targeting `01_web_app/app.py` routes and error handlers.
- Unit tests for reusable logic inside `01_web_app/services/` and helpers.

## Responsibilities
- Mirror the backend structure: when a new blueprint or service module is added, create matching tests.
- Use `pytest` fixtures to manage app and client setup.
- Keep tests deterministic and clean up artefacts written to `uploads/`.
- Focus on business rules such as validation, responses, and error handling.

## Workflow
1. Write or update tests alongside backend changes.
2. Run `pytest` from the repository root.
3. Share common setup in fixtures (`conftest.py`) when appropriate.
4. Update testing documentation when structure or tooling changes.

## Naming Conventions
- Test modules follow `test_*.py`.
- Helper modules use `snake_case`.

## Notes
Aim for thorough coverage of validation paths and extend the suite as storage backends or routes expand.
