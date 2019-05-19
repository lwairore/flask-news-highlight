import unittest
import headlines
Headlines = headlines.Headlines

class TestHeadlines(unittest.TestCase):
    """
    TestHeadlines sub-class defines test cases
    for the Headlines class behaviours.

    Args:
        unittest.TestCase: TestCase class helps in creating test cases.
    """
    
    def setUp(self):
        """
        Set up method to create a news_headlines instance
        before each test cases.
        """
        # Top_Headlines(author, title, description, url, urlToImage, publishedAt)
        news_headlines = Headlines(author, title, description, url, urlToImage, publishedAt)

    def tearDown(self):
        self.news_headlines = None

    def test_instance(self):
        """
        This method will only assert if self.news_headlines is an instance of
        Headlines class.
        """
        self.assertTrue(isinstance(self.news_headlines, Headlines)) 
