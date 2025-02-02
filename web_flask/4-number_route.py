#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB!"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """returns C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """returns Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


# a converter in the route to specify that the parameter should be an integer
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """returns n is a number only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
