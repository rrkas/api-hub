from flask import Flask


def create_app():
    app = Flask(__name__)
    app.app_context().push()

    from app.config import conf

    app.config.from_object(conf)

    from .main.routes import main_bp
    from .cetb.routes import cetb_bp
    from .prog.routes import prog_bp
    from .csv_gen.routes import csv_gen_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(cetb_bp)
    app.register_blueprint(prog_bp)
    app.register_blueprint(csv_gen_bp)

    return app
