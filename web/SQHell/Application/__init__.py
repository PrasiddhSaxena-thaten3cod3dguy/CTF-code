import sys
sys.dont_write_bytecode=True

from flask import Flask
from .db import setup
from os import urandom

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = urandom(24)

    setup()

    from .routes import routes
    app.register_blueprint(routes)

    return app