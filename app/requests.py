from app import app


api_key = app.config["NEWS_API_KEY"]
sources_url = app.config['SOURCES_BASE_API_URL']

def get_all_news_sources():
    """
    This function will be responsible for fetching/requesting all the
    news sources data. And the passing that data to be processed by
    process_all_news_sources_data() function. 
    get_all_news_sources() will finally return all the required news sources.
    """
    complete_sources_url = sources_url.format(api_key)