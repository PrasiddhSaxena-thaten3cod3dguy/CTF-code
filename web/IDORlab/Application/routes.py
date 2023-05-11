import jwt
import hashlib
from flask import Blueprint, make_response, redirect, render_template, request, flash, url_for
from .db import all_users, delete, query, query_user, add_user

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/login")
def login():
    return render_template("login.html")

@routes.route("/signup")
def signup():
    return render_template("signup.html")

@routes.route("/signup", methods=["POST"])
def signup_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        user = query_user(request.form["username"])
        if len(user) != 0:
            flash("User already exists.")
            return redirect(url_for("routes.signup"))
        else:
            add_user(request.form["username"], request.form["password"])
            flash("User successfully added.")
            return redirect(url_for("routes.login"))
    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.signup"))

@routes.route("/login", methods=["POST"])
def login_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        user = query(request.form["username"], request.form["password"])
        if len(user) == 0 or user[0][1] != hashlib.sha256(request.form["password"].encode()).digest().hex():
            flash("Incorrect login details.")
            return redirect(url_for("routes.login"))
        else:
            if request.form["username"] != "admin":
                payload = {"username": request.form["username"], "isAdmin": "false"}
            else:
                payload = {"username": request.form["username"], "isAdmin": "true"}
            secret = "secret" # My super secure secret ;)
            token = jwt.encode(payload, key=secret)
            resp = make_response(redirect(url_for("routes.home")))
            resp.set_cookie("auth", token)
            return resp
    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.login"))

@routes.route("/admin")
def admin():
    if "auth" in request.cookies.keys():
        try:
            payload = jwt.decode(request.cookies["auth"], key="secret", algorithms=["HS256",])
            #print(payload)
            if payload["isAdmin"] == "true":
                users = all_users()
                return render_template("admin.html", users=users)
            else:
                flash("Not authorized.")
                return redirect(url_for("routes.login"))
        except jwt.exceptions.InvalidSignatureError:
            flash("Not authorized.")
            return redirect(url_for("routes.login"))
    else:
        flash("Need to login first.")
        return redirect(url_for("routes.login"))

@routes.route("/admin/delete")
def user_delete():
    if "auth" in request.cookies.keys():
        try:
            payload = jwt.decode(request.cookies["auth"], key="secret", algorithms=["HS256",])
            if payload["isAdmin"] == "true":
                #delete op here
                if "id" in request.args.keys():
                    delete(request.args["id"])
                    return redirect(url_for("routes.admin"))
                else:
                    flash("What should I delete ?")
                    return redirect(url_for("routes.admin"))
            else:
                flash("Not authorized.")
                return redirect(url_for("routes.login"))
        except jwt.exceptions.InvalidSignatureError:
            flash("Not authorized.")
            return redirect(url_for("routes.login"))
    else:
        flash("Need to login first.")
        return redirect(url_for("routes.login"))

@routes.route("/logout")
def logout():
    if "auth" in request.cookies.keys():
        resp = make_response(redirect(url_for("routes.login")))
        resp.set_cookie("auth", "", expires=0)
        return resp
    else:
        flash("Need to login first.")
        return redirect(url_for("routes.login"))