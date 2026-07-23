from flask import Flask
from flask_migrate import Migrate
from config import Config
from .models import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import courses_bp
    app.register_blueprint(courses_bp)

    return app