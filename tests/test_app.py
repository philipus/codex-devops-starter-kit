from importlib import import_module
from pathlib import Path

import pytest
import io

# Add the 01_web_app directory to sys.path so we can import app
import sys
APP_DIR = Path(__file__).resolve().parents[1] / "01_web_app"
sys.path.insert(0, str(APP_DIR))

app_module = import_module("app")
app = app_module.create_app()

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def test_404_returns_json(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
    data = response.get_json()
    assert data == {"error": "Not Found"}


def test_500_returns_json(client):
    response = client.get("/error")
    assert response.status_code == 500
    data = response.get_json()
    assert data == {"error": "Internal Server Error"}


def test_upload_accepts_csv(client):
    data = {"file": (io.BytesIO(b"a,b\n1,2"), "test.csv")}
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 201
    assert response.get_json() == {"message": "File uploaded successfully"}
    uploaded = Path("uploads") / "test.csv"
    assert uploaded.exists()
    uploaded.unlink()


def test_upload_rejects_unsupported_type(client):
    data = {"file": (io.BytesIO(b"data"), "test.txt")}
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 400
    assert response.get_json() == {"error": "Unsupported file type"}


def test_upload_rejects_oversized_file(client):
    big_content = b"a" * (5 * 1024 * 1024 + 1)
    data = {"file": (io.BytesIO(big_content), "big.csv")}
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 413
    assert response.get_json() == {"error": "File too large"}
