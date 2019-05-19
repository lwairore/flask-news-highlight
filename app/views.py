from app import app
from flask import render_template
from .requests import get_all_news_sources

@app.route('/')
def index():
    """
    This function views the root page that returns index.html page
    and its data.
    """
    all_news_sources = get_all_news_sources()
    
    title = "Giko"
    return render_template("index.html", sources = all_news_sources, title = title)

@app.route('/source/<source>')
def news_healines(source):
    """
    This function retrieves live top and breaking headlines for a country.
    """
    return render_template('news_articles')

