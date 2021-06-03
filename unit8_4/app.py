import re
from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

messages = []

@app.route("/mypage/me")
def hello():
    return render_template("me.html")

@app.route("/mypage/contact")
def contact_page():
    if request.method =="GET":
        return render_template("name_form.html")
    elif request.method =="POST":
        #print(request.form)
        messages.append(request.form)
        return redirect("/mypage/me")

print(messages)