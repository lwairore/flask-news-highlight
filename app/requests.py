import urllib.request, json
from .models import Sources, Headlines, Everything, Business

# Keys
api_key = None
sources_url = None
everything_news_url = None
top_headlines_news_url = None
business_top_headlines_url = None

def configure_request(app):
    global api_key, sources_url, everything_news_url, top_headlines_news_url, business_top_headlines_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_API_URL']
    everything_news_url = app.config['EVERYTHING_BASE_API_URL']
    top_headlines_news_url = app.config['TOP_HEADLINES_BASE_API_URL']
    business_top_headlines_url = app.config['BUSINESS_TOP_HEADLINES']



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


def get_all_news_headlines(source):
    """
    This function will retrieve top-headlines news and passing the
    response it gets to process_all_headlines_data() function.
    """
    top_headlines_url = top_headlines_news_url.format(source, api_key )

    with urllib.request.urlopen(top_headlines_url) as url:
        headline_data = url.read()
        headlines_response = json.loads(headline_data)
        headlines_results = None
        if headlines_response['articles']:
            """
            Control flow filters out all empty sources.
            """
            headlines_items = headlines_response['articles']
            headlines_results = process_all_headlines_data(headlines_items)

    return headlines_results


def process_all_headlines_data(headlines_list):
    """
    This function is responsible for converting an data given as the Top-Headlines class.
    """
    headlines_processed_results = []
    for item in headlines_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        news_headlines = Headlines(author, title, description, url, urlToImage, publishedAt)
        headlines_processed_results.append(news_headlines)

    return headlines_processed_results

def get_everything_news():
    """
    This function will retrieve everything type news and passing the
    response it gets to process_all_everything_results() function.
    """
    everything_complete_url = everything_news_url.format(api_key)

    with urllib.request.urlopen(everything_complete_url) as url:
        everything_data = url.read()
        everything_response = json.loads(everything_data)
        everything_results = None

        if everything_response['articles']:
            everything_results_list = everything_response['articles']
            everything_results = process_all_everything_results(everything_results_list)

    return everything_results


def process_all_everything_results(everything_results_list):
    """
    This function is responsible for converting a data given as per Everything class.
    """
    everything_results = []
    for item in everything_results_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')

        everything_object = Everything(author, title, description, url, urlToImage, publishedAt)
        everything_results.append(everything_object)
        
    return everything_results

def get_business_headlines():
    """
    This function will retrieves business_headlines type news and passing the
    response it gets to process_all_everything_results() function.
    """
    business_headlines_complete_url = business_top_headlines_url.format(api_key)
    with urllib.request.urlopen(business_headlines_complete_url) as url:
        business_headlines_data = url.read()
        business_headlines_response = json.loads(business_headlines_data)
        business_headlines_results = None

        if business_headlines_response['articles']:
            business_headlines_results_list = business_headlines_response['articles']
            business_headlines_results = process_all_business_headlines_results(business_headlines_results_list)

    return business_headlines_results

def process_all_business_headlines_results(business_headlines_results_list):
    """
    This function is responsible for converting a data given as per Business class.
    """
    business_headlines_results = []
    for item in business_headlines_results_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')

        business_headlines_object = Business(author, title, description, url, urlToImage, publishedAt)
        business_headlines_results.append(business_headlines_object)
        
    return business_headlines_results

def search_articles(source):
    """
    This function passes in api_key and source name.
    Create the request and process the results.

    """
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(source, api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)
        search_article_results = None
        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_all_business_headlines_results(search_article_list)
    return search_article_results
        
