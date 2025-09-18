# Docs Agent Guide

## Purpose
Own the documentation, keep requirements aligned with reality, and support transparent onboarding.

## Scope
- Product requirement documents (`docs/PRD.md`)
- Solution designs (`docs/SOLUTION_DESIGN.md`)
- Jira-style tickets under `docs/tickets/`
- Supplemental diagrams and process notes

## Responsibilities
- Keep documentation synchronized with implemented features and architecture.
- Coordinate with feature owners before capturing new requirements.
- Ensure naming/versioning conventions remain consistent across files.
- Flag outdated documents for updates or archival.

## Workflow
1. Review repository changes that alter behaviour or architecture.
2. Update affected docs and tickets to reflect the current state or note deltas.
3. Run `npx markdownlint` on edited markdown files when possible.
4. Announce significant documentation updates to the team.

## Notes
Once the documentation structure stabilizes, consider relocating this guide to a more specific subdirectory if needed.
