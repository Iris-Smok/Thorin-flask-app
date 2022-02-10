"""
Flask
"""
import os
from flask import Flask, render_template  # Import the Flask class


app = Flask(__name__)


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
    return render_template("about.html", page_title="About")


@app.route("/contact")
def contact():
    """
     Contact page
    """
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
