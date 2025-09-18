# Contributor Guide

## Purpose
Main coordination guide for agents contributing to this DevOps starter project. Provides an overview of the folder structure, agent responsibilities, and contribution conventions.

## Folder Overview
- `01_web_app/`: Flask-based backend web app and business logic (includes frontend).
- `02_github_basics/`: GitHub usage tutorials and configuration.
- `03_dev_team_workflow/`: Team collaboration workflows (e.g. PRs, branches).
- `04_extras/`: Optional utilities, enhancements, and add-ons.
- `data/`: Data samples used for testing and development.
- `uploads/`: Directory for file uploads (e.g., via the upload endpoint).
- `tests/`: Pytest-based tests for verifying app functionality.

## Agent Responsibilities
- 📄 Keep `README.md` and `AGENTS.md` files updated as features evolve.
- 📁 Maintain clear folder structure and respect separation of concerns.
- 🔧 Ensure that new scripts, tests, or features follow naming conventions.
- 🧪 Validate changes locally before pushing, using `pytest` and any defined CI workflows.
- 📬 Communicate through pull requests with meaningful commit messages and descriptions.
- 🧭 Route subfolder-specific tasks to:
  - `01_web_app/backend/AGENTS.md`
  - `01_web_app/frontend/AGENTS.md`
  - `docs/AGENTS.md` (optional, if documentation becomes complex)

## Dev Environment
- Use **Python 3.11+**
- Dependencies managed via `requirements.txt`
- Format Markdown files with:  
  `npx markdownlint README.md`
- Run all tests:  
  `pytest`

## PR Instructions
- Title format: `[folder] Brief description`
- Always include test coverage for new features.
- Link related issues or tasks, if applicable.

## Notes
This agent routes coordination across the entire repository and maintains consistency between sub-agents.
