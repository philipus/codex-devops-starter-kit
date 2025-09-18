# Solution Design

## Stack
- **Backend:** Flask + Gunicorn
- **Frontend:** React + Vite + TailwindCSS

---

## 🗃️ Storage

- **Local File System** (default):
  - Files (e.g., uploads) are saved to `./uploads/` during development.
  - This avoids external dependencies and simplifies testing.
  
- **Storage Abstraction Layer**:
  - Long-term goal: route storage operations through `services/storage_service.py`.
  - Enables future support for cloud backends (e.g., S3, Azure Blob) by swapping the implementation once the abstraction is in place.

- **Future Enhancement**:
  - Add support for configurable storage backends using `.env`:
    ```env
    STORAGE_BACKEND=local  # or 's3', 'azure'
    ```

---

## ⚙️ Infrastructure

- **Lightweight Python/Flask App**:
  - Entry point: `python app.py` or `flask run`
  - No container or Kubernetes dependency required for local dev

- **Config via `.env` file**:
  - Manages environment variables for storage paths, secrets, and backend switches
  - Keeps deployment targets flexible (Docker, Render, Railway, etc.)

- **Optional Deployment Aids** (for later):
  - `supervisor` or `systemd` for background process management
  - GitHub Actions or `pre-commit` for CI, linting, and tests

---

## Key Design Principles

- ✅ **Modular by Design**: Codebase structured to enable parallel work across routes, services, and components
- 🧱 **Clear Separation of Concerns**:
  - Route logic currently lives in `app.py`; migrate into `backend/routes/` as new blueprints are introduced.
  - Business logic in `services/`
  - HTML/CSS in `frontend/`
- 🚨 **Error Handling**: Flask `@errorhandler` decorators defined in `app.py`, with the option to move helpers into `exceptions.py` when the surface grows
- 🧪 **Testable Services**: Each logic layer (e.g., file handling) is isolated and independently testable
