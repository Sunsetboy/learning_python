from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world 2!!"

@app.route("/user/<username>")
def show_profile(username):
    return f"Hello {escape(username)}"
