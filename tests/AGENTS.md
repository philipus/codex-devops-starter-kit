# Test Guide

## Purpose
This folder contains automated tests to verify the functionality and stability of the application.

## Agent Responsibilities

- Write tests for every major feature added in `01_web_app/` (especially `api/` and `services/`).
- Use the `pytest` framework. Tests must be runnable via:

  ```bash
  pytest
  ```

  from the project root.

- Organize tests by domain or module, mirroring the structure of `01_web_app/backend/`.
- Use the naming convention: `test_*.py`.
- Ensure tests are self-contained:
  - Clean up any temporary files or generated artifacts.
  - Avoid relying on shared mutable state.
- Focus on testing business logic, API behavior, and edge cases.
- Do not test internal framework mechanics (e.g., `__pycache__`, Flask internals).

## Notes

- Consider using fixtures for reusable setup.
- Run all tests before opening a pull request.
- Expand test coverage as features grow.
