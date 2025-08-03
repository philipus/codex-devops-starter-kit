from __future__ import annotations

from pathlib import Path
from typing import Optional

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from exceptions import ValidationError

ALLOWED_EXTENSIONS = {".csv", ".pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


def save_file(file: Optional[FileStorage], upload_dir: Path) -> str:
    """Validate and save an uploaded file.

    Args:
        file: The uploaded file from the request.
        upload_dir: Directory where the file should be saved.

    Returns:
        The filename of the saved file.

    Raises:
        ValidationError: If validation fails.
    """
    if file is None or file.filename == "":
        raise ValidationError("No file provided")

    filename = secure_filename(file.filename)
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError("Unsupported file type")

    file.seek(0, 2)  # move to end of file
    size = file.tell()
    file.seek(0)
    if size > MAX_FILE_SIZE:
        raise ValidationError("File too large")

    upload_dir.mkdir(parents=True, exist_ok=True)
    filepath = upload_dir / filename
    file.save(filepath)
    return filename
