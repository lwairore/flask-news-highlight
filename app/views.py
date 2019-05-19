from app import app


@app.route('/')
def index():
    """
    This function views the root page that returns index.html page
    and its data.
    """
    