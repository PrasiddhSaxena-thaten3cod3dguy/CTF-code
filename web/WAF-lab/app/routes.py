from flask import Blueprint, redirect, render_template, request, url_for
from .utils import find_subdomains

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/", methods=["POST"])
def home_post():
    if "domain" in request.form.keys():
        return render_template("index.html", output=find_subdomains(request.form["domain"]))
    else:
        return redirect(url_for("routes.home"))