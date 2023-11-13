from flask import Flask
from .extensions import db
from .config import Config

def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    db.init_app(app)

    from flaskr.auth import bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from flaskr.main import bp as server_blueprint
    app.register_blueprint(server_blueprint)
    return app