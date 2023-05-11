from flask import Flask
from os import urandom

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = urandom(24)

    from .db import setup
    setup()

    from .routes import routes
    app.register_blueprint(routes)

    return app