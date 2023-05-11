from __future__ import unicode_literals
from enum import unique
from . import db

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    desc = db.Column(db.String(100))