from flask import Blueprint, redirect, render_template, request, send_file, url_for

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/file_rdhgiuhriu")
def getfile():
    if "file" in request.args.keys():
        filename = request.args["file"]
        try:
            return send_file(filename, as_attachment=True)
        except:
            return "Error in getting the file."
    else:
        return redirect(url_for("routes.index"))