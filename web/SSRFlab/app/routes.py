import hashlib
from flask import Blueprint, flash, redirect, render_template, request, url_for
from .utils import get_img_from_link
from .db import add_data, query_all, query_username

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/signup")
def signup():
    return render_template("signup.html")

@routes.route("/signup", methods=["POST"])
def signup_post():
    if "username" in request.form.keys() and "password" in request.form.keys() and "url" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]

        user = query_username(username)
        if len(user) != 0:
            flash("User already exists")
            return redirect(url_for("routes.signup"))
        else:
            url = get_img_from_link(request.form["url"])
            if url == "malicious":
                flash("Hacker detected.")
                return redirect(url_for("routes.signup"))
            add_data(username, password, url)

            flash("User added successfully.")
            return redirect(url_for("routes.index"))

    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.signup"))

@routes.route("/", methods=["POST"])
def index_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]

        user = query_all(username)
        if len(user) == 0 or user[0][1] != hashlib.sha256(password.encode()).digest().hex():
            flash("Incorrect details.")
            return redirect(url_for("routes.index"))
        else:
            return render_template("dashboard.html", user=username, img_url=user[0][2].replace("app", ""))
    else:
        flash("Invalid parameters")
        return redirect(url_for("routes.index"))