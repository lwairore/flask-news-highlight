from app import app
from flask import render_template
from .requests import get_all_news_sources as news_sources

@app.route('/')
def index():
    """
    This function views the root page that returns index.html page
    and its data.
    """
    all_news_sources = news_sources()
    title = "Giko"
    return render_template("index.html", sources = all_news_sources, title = title)
