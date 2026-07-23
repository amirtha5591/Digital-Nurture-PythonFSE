from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register our modular routes blueprint
    from .routes import courses_bp
    app.register_blueprint(courses_bp)

    return app