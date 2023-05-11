from flask import Blueprint, flash, redirect, render_template, request, url_for
from .utils import find_ip

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/", methods=["POST"])
def home_post():
    if "domain" in request.form.keys():
        return render_template("index.html", output=find_ip(request.form["domain"]))
    else:
        flash("Invalid parameters.")
        return redirect(url_for("routes.home"))