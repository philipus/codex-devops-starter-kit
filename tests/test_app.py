from importlib import import_module
from pathlib import Path

import pytest

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
