import re
from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route("/mypage/me", methods=["GET", "POST"])
def hello():
    if request.method=="GET":
        return render_template("me.html")
    elif request.method=="POST":
        return redirect("/mypage/contact")

@app.route("/mypage/contact", methods=["GET", "POST"])
def contact_page():
    if request.method =="GET":
        return render_template("name_form.html")
    elif request.method =="POST":
        message = request.form
        print("here")
        return redirect("/mypage/me")
