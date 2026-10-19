from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def first():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/")
def index():
    

if __name__ == "__main__":
    app.run(debug=True) 