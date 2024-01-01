#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """returns a list of all states in the database"""
    from models import storage
    from models.state import State

    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """returns a list of all states in the database"""
    from models import storage
    from models.state import State

    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state, mode="id")
    return render_template("9-states.html", states=None, mode="id")


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session"""
    from models import storage

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
