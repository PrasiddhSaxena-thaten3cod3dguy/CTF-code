from flask import Flask, render_template,request,flash,render_template_string,redirect,url_for
import jwt

app=Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_TYPE"] = "filesystem"
jwtsecret="YOUFOUNDMYSECRETKEYTHISISNOTFAIRATALL"

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        flash("Try to be a real clown!!")
        return render_template("login.html")

@app.route("/prayorprey",methods=["POST","GET"])
def prayorprey():
    if request.method=="GET":
        return render_template("search.html")
    prayer=request.form.get("prayer")
    return render_template_string(prayer)

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if "auth" in request.cookies.keys():
        global jwtsecret
        token=request.cookies["auth"]
        try:
            payload=jwt.decode(token,jwtsecret,algorithms=["HS256",])
            if payload["user"]=="notaclown":
                return render_template("dashboard.html")
            else:
                flash("Clown Clown Everywhere!!")
                return redirect(url_for("login"))
        except Exception as e:
            flash("Clown!!")
            return redirect(url_for("login"))           
    else:
        flash("You Are A Real Clown!!!")
        return redirect(url_for("login"))


app.run(host="0.0.0.0",port=3000,debug=True)
