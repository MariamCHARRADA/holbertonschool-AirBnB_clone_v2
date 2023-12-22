#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """returns a list of all states in the database"""
    from models import storage

    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session"""
    from models import storage

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
