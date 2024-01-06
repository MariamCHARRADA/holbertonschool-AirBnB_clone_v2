#!/usr/bin/python3
"""a script that starts a Flask web application and
display a HTML page like 6-index.html,which was done
during the project AirBnB clone - Web static"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def show():
    """ display a HTML page like 6-index.html,
    which was done during the project
    AirBnB clone - Web static"""
    from models.amenity import Amenity
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")