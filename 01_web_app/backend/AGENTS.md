# 01_web_app/backend Agent Guide

## Purpose
This folder contains the main web application built with Flask. It is structured for modularity and clean separation of concerns, enabling agents to work in parallel without collisions.

## Folder Structure and Responsibilities

- `main.py`  
  - 🔌 Entry point that initializes the Flask app and registers blueprints.

- `api/`  
  - 📡 Route logic (Flask blueprints).  
  - Each feature (e.g., file upload) gets its own route module.
  - Keep route handlers thin—delegate logic to the `services/` layer.

- `services/`  
  - 🧠 Business logic and orchestration.
  - Handle validation, computation, file processing, etc.
  - Functions should be testable and avoid side effects.

- `core/`  
  - ⚙️ Configuration, constants, and utility functions.
  - Helps centralize app-wide settings and avoid hardcoding.

- `errors/`  
  - 🚨 Custom exception classes and error handling.
  - Add new exceptions consistently with existing patterns.

- `models/` *(Optional)*  
  - 🗂️ Pydantic schemas or future ORM models.

## Agent Guidelines

- 👣 Respect separation of concerns:
  - `api/` for routes only.
  - `services/` for logic.
  - `core/` for config.
- ✅ Add/update unit tests for all new `services/` functions or `api/` routes.
- 🧪 Run `pytest` to validate changes.
- 🚫 Avoid global state unless placed in `core/`.
- 🧹 Format Python code with `black`.
- 📄 Keep `README.md` and `AGENTS.md` up to date after changes.
- 🧰 Use `npx markdownlint README.md` to lint Markdown files.

## Example Contribution Workflow

1. Create or update a route in `api/`.
2. Add supporting logic in `services/`.
3. Add custom exceptions in `errors/` if needed.
4. Add or update tests in `tests/`.
5. Update documentation in `README.md`.

## Naming Conventions

- Use `snake_case` for files and function names.
- Name route files after the domain they handle (e.g., `upload.py`, `auth.py`).

## Notes

This folder acts as the **backend** of the web application. Frontend-related logic belongs in `01_web_app/frontend/`.