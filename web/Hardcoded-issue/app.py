import sys
sys.dont_write_bytecode=True

import jwt
import hashlib
from flask import Flask, flash, make_response, redirect, render_template, request, url_for
from db import query_login, setup_db
from os import urandom, getenv, popen

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(24)

@app.route("/dashboard")
def dashboard():
    if "auth" in request.cookies.keys():
        token = request.cookies["auth"]
        secret = getenv("JWT_SECRET_KEY")
        try:
            payload = jwt.decode(token, key=secret, algorithms=["HS256",])
            if payload["user"] == "admin":
                if "cmd" in request.args.keys():
                    cmd = request.args["cmd"]
                    blacklist = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '\\', '"', ';', ':', '?', '>', '<', ',', 'whoami', 'cat', 'ls', 'flag', 'etc', 'passwd', 'shadow']
                    if any([x in cmd for x in blacklist]):
                        flash("Hacker detected.")
                        return redirect(url_for("dashboard", cmd=""))
                    return render_template("dashboard.html", cmd=popen(cmd).read())
                return render_template("dashboard.html", cmd="")
            else:
                return redirect(url_for("index"))
        except:
            flash("Not authorized.")
            return redirect(url_for("login"))
    else:
        flash("Login to access dashboard.")
        return redirect(url_for("login"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]
        user = query_login(username)
        if len(user) == 0 or user[0][1] != hashlib.sha256(password.encode()).digest().hex():
            flash("Incorrect details.")
            return redirect(url_for("login"))
        else:
            secret = getenv("JWT_SECRET_KEY")
            payload = {"user": "admin"}
            token = jwt.encode(payload, key=secret)
            resp = make_response(redirect(url_for("dashboard")))
            resp.set_cookie("auth", token)
            return resp
    else:
        flash("Incorrect parameters.")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "auth" in request.cookies.keys():
        resp = make_response(redirect(url_for("login")))
        resp.set_cookie("auth", "", expires=0)
        return resp
    else:
        flash("Please login first.")
        return redirect(url_for("login"))

@app.route("/image")
def image():
    if "file" in request.args.keys():
        file = request.args["file"]
        if not file.startswith("static/img/"):
            return redirect(url_for("index"))
        out_filename = file.split("/")[-1]
        with open(file, "rb") as rf:
            content = rf.read()
        data = make_response(content)
        data.headers['Content-Type'] = 'application/octet-stream'
        data.headers['Content-Disposition'] = f'attachment; filename={out_filename}'
        return data
    else:
        return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    setup_db()
    app.run("0.0.0.0", port=80)