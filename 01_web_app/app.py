"""Minimal Flask application with basic error handling."""

from pathlib import Path

from flask import Flask, jsonify, request
from werkzeug.exceptions import RequestEntityTooLarge

from exceptions import ValidationError
from services.file_service import save_file


UPLOAD_DIR = Path(__file__).resolve().parents[1] / "uploads"


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB

    @app.route('/')
    def home() -> str:
        """Root route returning a friendly greeting."""
        return 'Hello Codex'

    @app.route('/error')
    def trigger_error() -> None:  # pragma: no cover - used only for tests
        """Route used in tests to simulate an internal error."""
        raise RuntimeError('Intentional error')

    @app.route('/upload', methods=['POST'])
    def upload():
        """Handle file upload requests."""
        app.logger.info("Upload attempt")
        try:
            save_file(request.files.get('file'), UPLOAD_DIR)
        except ValidationError as exc:
            app.logger.warning("Upload failed: %s", exc)
            return jsonify({'error': str(exc)}), 400
        app.logger.info("Upload succeeded")
        return jsonify({'message': 'File uploaded successfully'}), 201

    @app.errorhandler(RequestEntityTooLarge)
    def file_too_large(error):
        """Return a JSON 413 error when the uploaded file is too large."""
        app.logger.warning("Upload failed: file too large")
        return jsonify({'error': 'File too large'}), 413

    @app.errorhandler(404)
    def not_found(error):
        """Return a JSON 404 error response."""
        return jsonify({'error': 'Not Found'}), 404

    @app.errorhandler(Exception)
    def internal_error(error):
        """Return a JSON 500 error response for unhandled exceptions."""
        app.logger.exception(error)
        return jsonify({'error': 'Internal Server Error'}), 500

    return app


app = create_app()

if __name__ == '__main__':  # pragma: no cover - manual execution
    app.run(debug=True)
