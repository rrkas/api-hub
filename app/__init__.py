from flask import Flask

from app.config import conf


def create_app():
    app = Flask(__name__)
    app.config.from_object(conf)

    from .main.routes import main_bp
    from .cetb.routes import cetb_bp
    from .prog.routes import prog_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(cetb_bp)
    app.register_blueprint(prog_bp)

    return app
