"""
Flask
"""
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# Import the Flask class
# request library from Flask. Is going to handle things like finding out what
# method we used, and it will also contain our object when we posted it
# to use flashed messages, we need to create a secret key, because Flask
# cryptographically signs all of the messages for security purpose


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    """
     function called index, which returns the string Hello World
     when we try to browse to the root directory, as indicated
     by the "/", then Flask triggers the index function underneath
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
     About page
    """
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    """
     URL
    """
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
     Contact page
    """
    if request.method == "POST":
        # this is a dictionary
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """
     Careers page
    """
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
