import sys
sys.dont_write_bytecode=True

from flask import Flask
from os import urandom
from .db import setup

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = urandom(24)
    app.config["SESSION_COOKIE_HTTPONLY"] = False

    from .routes import routes
    app.register_blueprint(routes)

    setup()

    return app