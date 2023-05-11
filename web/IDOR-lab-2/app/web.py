from flask import Blueprint, render_template

web = Blueprint("web", __name__)

@web.route("/")
def home():
    return render_template("index.html")

@web.route("/login")
def index():
    return render_template("login.html")

@web.route("/signup")
def signup():
    return render_template("signup.html")