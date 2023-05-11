from flask import Blueprint, flash, make_response, redirect, render_template, request, url_for
from .db import *
import jwt

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return redirect(url_for("routes.login"))

@routes.route("/blog")
def blog():
    if "auth" in request.cookies.keys():
        payload = jwt.decode(request.cookies["auth"], key="mysupersecureelitekeynoonecancrack", algorithms=['HS256', ])
        username = payload["user"]
        q = query_username(username)
        user = []
        for i in q:
            user.append(i[0])

        return render_template("blog.html", user=user)
    else:
        flash("Need to login first.")
        return redirect(url_for("routes.login"))

@routes.route("/login")
def login():
    return render_template("login.html")

@routes.route("/login", methods=["POST"])
def login_post():
    
    if "username" in request.form.keys() and "password" in request.form.keys():
        
        username = request.form["username"]
        password = request.form["password"]

        q = query(username, password)
        if len(q) == 0:
            flash("Invalid credentials.")
            return redirect(url_for("routes.login"))
        else:
            token = jwt.encode({"user":username}, key="mysupersecureelitekeynoonecancrack")
            resp = make_response(redirect(url_for("routes.blog")))
            resp.set_cookie("auth", token)
            return resp
    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.login"))


@routes.route("/signup")
def signup():
    return render_template("signup.html")

@routes.route("/signup", methods=["POST"])
def signup_post():

    if "username" in request.form.keys() and "password" in request.form.keys():
        
        blacklist = ["union", "select", "order", "form", "UNION", "SELECT", "ORDER", "FROM"]

        for word in blacklist:
            if word in request.form["username"] or word in request.form["password"]:
                flash("Hacker detected.")
                return redirect(url_for("routes.signup"))

        username = request.form["username"]
        password = request.form["password"]

        q = query_username_secure(username)
        if len(q) != 0:
            flash("User already exists.")
        else:
            add_user(username, password)
            flash("User added successfully.")
            return redirect(url_for("routes.login"))

        return redirect(url_for("routes.signup"))
    
    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.signup"))

@routes.route("/logout")
def logout():
    if "auth" in request.cookies.keys():
        resp = make_response(redirect(url_for("routes.login")))
        resp.set_cookie("auth", "", expires=0)
        return resp
    else:
        flash("Need to login first.")
        return redirect(url_for("routes.login"))