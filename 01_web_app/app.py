"""Minimal Flask application with basic error handling."""

from flask import Flask, jsonify


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route('/')
    def home() -> str:
        """Root route returning a friendly greeting."""
        return 'Hello Codex'

    @app.route('/error')
    def trigger_error() -> None:  # pragma: no cover - used only for tests
        """Route used in tests to simulate an internal error."""
        raise RuntimeError('Intentional error')

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
