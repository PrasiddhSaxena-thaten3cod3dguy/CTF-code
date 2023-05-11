from flask import Blueprint, redirect, render_template, request, flash, url_for
from .utils import parse_xml
from . import db
from .models import Todo

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html", todos=Todo.query.all())

@routes.route("/create")
def create():
    return render_template("addTODO.html")

@routes.route("/create", methods=["POST"])
def create_post():
    if request.data:
        data = parse_xml(request.data.decode('utf-8'))
        if "title" in data.keys() and "desc" in data.keys():
            todo = Todo(title=data["title"], desc=data["desc"])
            if Todo.query.filter_by(title=data["title"]).first():
                flash("Todo already exists.")
                return redirect(url_for("routes.index"))
            db.session.add(todo)
            db.session.commit()
            flash("Todo added successfully.")
            return redirect(url_for("routes.index"))
    flash("Error somewhere")
    return redirect(url_for("routes.index"))

@routes.route("/delete")
def delete():
    if "id" in request.args.keys():
        todo = Todo.query.filter_by(id=request.args["id"])
        if not todo.first():
            flash("TODO does not exist.")
            return redirect(url_for("routes.index"))

        todo.delete()
        db.session.commit()
        return redirect(url_for("routes.index"))
    else:
        flash("Can not delete nothing.")
        return redirect(url_for("routes.index"))