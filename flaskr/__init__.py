from flask import Flask
from .extensions import db
from .config import Config

def create_app(config_class=Config):
    """"Configuring Flask app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    app.secret_key = 'mattgottasack'
    app.config['SESSION_TYPE'] = 'filesystem'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from flaskr.auth.routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from flaskr.main.routes import server as server_blueprint
    app.register_blueprint(server_blueprint)
    return app