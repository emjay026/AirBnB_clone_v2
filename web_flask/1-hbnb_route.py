#!/usr/bin/python3
"""This module implements a Flask application."""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Implements the root web route."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Implements the root web route."""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
