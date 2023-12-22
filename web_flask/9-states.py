#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """returns a list of all states in the database"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)

@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """returns a list of all states in the database"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)

@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
