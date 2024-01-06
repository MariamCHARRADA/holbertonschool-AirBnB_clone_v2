#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page"""
    from models import storage
    from models.state import State
    from models.amenity import Amenity

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session"""
    from models import storage

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
