from app import app
from flask import render_template


@app.route('/')
def index():
    """
    This function views the root page that returns index.html page
    and its data.
    """
    return render_template("index.html")
