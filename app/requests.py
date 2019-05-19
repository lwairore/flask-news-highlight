from app import app
import urllib.request, json
from .models import sources

Sources = sources.Sources
api_key = app.config["NEWS_API_KEY"]
sources_url = app.config['SOURCES_BASE_API_URL']
everything_news_url = app.config['EVERYTHING_BASE_API_URL']
top_headlines_news_url = app.config['TOP_HEADLINES_BASE_API_URL']

def process_all_news_sources_data(sources_list):
    """
    This function will process the sources response as per Sources class arguments;
    Each source will be required to have an id, name, url, country, and description.
    """
    sources_processed_results = []
    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        url = item.get('url')
        country = item.get('country')
        description = item.get('description')
        new_source = Sources(id, name, url, country, description)
        sources_processed_results.append(new_source)

    return sources_processed_results


def get_all_news_sources():
    """
    This function will be responsible for fetching/requesting all the
    news sources data. And the passing that data to be processed by
    process_all_news_sources_data() function. 
    get_all_news_sources() will finally return all the required news sources.
    """
    complete_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(complete_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        sources_results = None
        if sources_response['sources']:
            """
            Control flow filters out all empty sources.
            """
            sources_items = sources_response['sources']
            sources_results = process_all_news_sources_data(sources_items)

    return sources_results


