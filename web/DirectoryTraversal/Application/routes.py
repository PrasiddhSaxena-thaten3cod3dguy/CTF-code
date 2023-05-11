from flask import Blueprint, flash, make_response, redirect, render_template, request, url_for

routes = Blueprint("routes", __name__)
BROCHURE = "Application/static/uploads/Brochure.pdf"
APPLICATION = "Application"

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/error")
def error():
    return render_template("error.html")

@routes.route("/brochure", methods=["GET", "POST"])
def download_brochure():
    if request.method == "GET":
        if "path" not in request.args.keys():
            with open(BROCHURE, "rb") as rf:
                content = rf.read()
            data = make_response(content)
            data.headers['Content-Type'] = 'application/octet-stream'
            data.headers['Content-Disposition'] = 'attachment;'
            return data
        else:
            flash("Waf w00f in action.")
            return redirect(url_for("routes.index"))
    else:
        if "path" not in request.form.keys() or not request.form["path"].startswith("/static/uploads"):
            flash("Waf w00f in action.")
            return redirect(url_for("routes.index"))
        else:
            out_filename = request.form["path"].split("/")[-1]
            file = f"{APPLICATION}{request.form['path']}"
            try:
                with open(file, 'rb') as rf:
                    content = rf.read()
                data = make_response(content)
                data.headers['Content-Type'] = 'application/octet-stream'
                data.headers['Content-Disposition'] = f'attachment; filename={out_filename}'
                return data
            except:
                return redirect(url_for("routes.error"))
