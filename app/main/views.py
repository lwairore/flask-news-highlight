from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_all_news_sources, get_all_news_headlines, get_everything_news, get_business_headlines, search_articles

@main.route('/')
def index():
    """
    This function views the root page that returns index.html page
    and its data.
    """
    all_news_sources = get_all_news_sources()
    everything_news_items = get_everything_news()
    business_headliness = get_business_headlines()
    title = "Giko"
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search', source_name = search_article))
    else:
        return render_template("index.html", sources = all_news_sources, title = title, others = everything_news_items, business_headliness = business_headliness)

@main.route('/source/<source>')
def news_healines(source):
    """
    This function retrieves live top and breaking headlines for a country.
    """
    title = "Giko"
    news_healines = get_all_news_headlines(source)
    return render_template('news_articles.html', headlines = news_healines)

@main.route('/search/<source_name>')
def search(source_name):
    """
    View function to display search results.
    """
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_articles(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html', results = searched_sources)