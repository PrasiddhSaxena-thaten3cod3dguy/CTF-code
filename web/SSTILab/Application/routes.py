from flask import Blueprint, flash, redirect, render_template, render_template_string, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, login_required, logout_user
from .models import User
from . import db

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return redirect(url_for("routes.blog"))

@routes.route("/blog")
@login_required
def blog():
    with open("Application/templates/blog.html", "r") as rf:
        content = rf.read().replace("$user$", current_user.username)
    return render_template_string(content)

@routes.route("/login")
def login():
    return render_template("login.html")

@routes.route("/login", methods=["POST"])
def login_post():
    if "username" in request.form.keys() and "password" in request.form.keys():

        user = User.query.filter_by(username=request.form["username"]).first()

        if not user or not check_password_hash(user.password, request.form["password"]):
            flash("Invalid credentials.")
            return redirect(url_for("routes.login"))

        login_user(user, remember=True)
        return redirect(url_for("routes.blog"))

    else:

        flash("Invalid parameters.")
        return redirect(url_for("routes.login"))

@routes.route("/register")
def register():
    return render_template("register.html")

@routes.route("/register", methods=["POST"])
def register_post():
    if "username" in request.form.keys() and "password" in request.form.keys():

        blacklist = ["'", "&", "`", "open", "config", "ls", "id", "etc", "passwd", "os", "popen" , "cat", "subprocess", "import", "system", "execute", "eval"]

        for word in blacklist:
            if word in request.form["username"] or word in request.form["password"]:
                flash("Hacker detected.")
                return redirect(url_for("routes.register"))

        if User.query.filter_by(username=request.form["username"]).first():
            flash("User already exists.")
            return redirect(url_for("routes.register"))

        user = User(username=request.form["username"], password=generate_password_hash(request.form["password"], method="sha256"))
        db.session.add(user)
        db.session.commit()

        flash("User successfully added.")
        return redirect(url_for("routes.login"))

    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.register"))

@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("routes.login"))