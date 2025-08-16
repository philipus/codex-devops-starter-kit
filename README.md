# codex-devops-starter-kit

## File Upload API

This project includes a minimal Flask application that accepts file uploads and stores them on disk.

### Endpoint

**POST** `/upload` — upload a single file to the server.

### Usage

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
python 01_web_app/app.py
```

3. Send a file with curl:

```bash
curl -X POST -F "file=@path/to/report.csv" http://localhost:5000/upload
```

The file is saved to the `uploads/` directory. The folder is created automatically if it does not exist.

### Validation rules

- Allowed extensions: `.csv` and `.pdf`
- Maximum size: 5 MB

### Responses

- `201 {"message": "File uploaded successfully"}` for a valid upload.
- `400 {"error": "<reason>"}` for missing files or unsupported types.
- `413 {"error": "File too large"}` when the file exceeds the size limit.

