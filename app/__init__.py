from flask import Flask

from app.config import conf


def create_app():
    app = Flask(__name__)
    app.config.from_object(conf)

    from .main.routes import main_bp

    app.register_blueprint(main_bp)

    return app
