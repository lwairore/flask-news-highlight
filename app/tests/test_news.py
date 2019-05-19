import unittest
import business_headlines

Business = business_headlines.Business

class TestBusiness(unittest.TestCase):
    """
    TestBusiness sub-class defines test cases
    for the Business class behaviours.

    Args:
        unittest.TestCase: TestCase class helps in creating test cases.
    """
    
    def setUp(self):
        """
        Set up method to create a news_business_headlines instance
        before each test cases.
        """        
        self.news_business_headlines = Business("John F.L", "Deep African White Gold", "Ugali, African Prestige meal. Staple food in countries such as Kenya....", "https://www.google.io/img/Africa", "http://www.google.io/img/ugali", "2000-19-03")


    def tearDown(self):
        self.news_business_headlines = None

    def test_instance(self):
        """
        This method will only assert if self.news_business_headlines is an instance of
        Business class.
        """
        self.assertTrue(isinstance(self.news_business_headlines, Business)) 

    def test_init_author(self):
        """
        This test case tests if self.news_business_headlines.author is initialized
        properly.
        """
        self.assertEqual(self.news_business_headlines.author, "John F.L")

    def test_init_title(self):
        """
        This test case tests if self.news_business_headlines.title is initialized
        properly.
        """
        self.assertEqual(self.news_business_headlines.title, "Deep African White Gold")

    def test_init_description(self):
        """
        This test case tests if self.news_business_headlines.description is initialized
        properly.
        """
        self.assertEqual(self.news_business_headlines.description, "Ugali, African Prestige meal. Staple food in countries such as Kenya....")

    def test_init_url(self):
        """
        This test case tests if self.news_business_headlines.url is initialized
        properly.
        """
        self.assertEqual(self.news_business_headlines.url, "https://www.google.io/img/Africa")

    def test_init_urlToImage(self):
        """
        This test case tests if self.news_business_headlines.urlToImage is initialized
        properly.
        """
        self.assertEqual(self.news_business_headlines.urlToImage, "http://www.google.io/img/ugali")

    def test_init_publishedAt(self):
        """
        This test case tests if self.news_business_headlines.publishedAt is initialized
        properly.
        """
        self.assertEqual(self.news_business_headlines.publishedAt, "2000-19-03")

import everything
Everything = everything.Everything

class TestEverything(unittest.TestCase):
    """
    TestEverything sub-class defines test cases
    for the Everything class behaviours.

    Args:
        unittest.TestCase: TestCase class helps in creating test cases.
    """
    
    def setUp(self):
        """
        Set up method to create a everything_instance instance
        before each test cases.
        """        
        self.everything_instance = Everything("John F.L", "Deep African White Gold", "Ugali, African Prestige meal. Staple food in countries such as Kenya....", "https://www.google.io/img/Africa", "http://www.google.io/img/ugali", "2000-19-03")


    def tearDown(self):
        self.everything_instance = None

    def test_instance(self):
        """
        This method will only assert if self.everything_instance is an instance of
        Everything class.
        """
        self.assertTrue(isinstance(self.everything_instance, Everything)) 

    def test_init_author(self):
        """
        This test case tests if self.everything_instance.author is initialized
        properly.
        """
        self.assertEqual(self.everything_instance.author, "John F.L")

    def test_init_title(self):
        """
        This test case tests if self.everything_instance.title is initialized
        properly.
        """
        self.assertEqual(self.everything_instance.title, "Deep African White Gold")

    def test_init_description(self):
        """
        This test case tests if self.everything_instance.description is initialized
        properly.
        """
        self.assertEqual(self.everything_instance.description, "Ugali, African Prestige meal. Staple food in countries such as Kenya....")

    def test_init_url(self):
        """
        This test case tests if self.everything_instance.url is initialized
        properly.
        """
        self.assertEqual(self.everything_instance.url, "https://www.google.io/img/Africa")

    def test_init_urlToImage(self):
        """
        This test case tests if self.everything_instance.urlToImage is initialized
        properly.
        """
        self.assertEqual(self.everything_instance.urlToImage, "http://www.google.io/img/ugali")

    def test_init_publishedAt(self):
        """
        This test case tests if self.everything_instance.publishedAt is initialized
        properly.
        """
        self.assertEqual(self.everything_instance.publishedAt, "2000-19-03")

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
        self.news_headlines = Headlines("John F.L", "Deep African White Gold", "Ugali, African Prestige meal. Staple food in countries such as Kenya....", "https://www.google.io/img/Africa", "http://www.google.io/img/ugali", "2000-19-03")


    def tearDown(self):
        self.news_headlines = None

    def test_instance(self):
        """
        This method will only assert if self.news_headlines is an instance of
        Headlines class.
        """
        self.assertTrue(isinstance(self.news_headlines, Headlines)) 

    def test_init_author(self):
        """
        This test case tests if self.news_headlines.author is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.author, "John F.L")

    def test_init_title(self):
        """
        This test case tests if self.news_headlines.title is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.title, "Deep African White Gold")

    def test_init_description(self):
        """
        This test case tests if self.news_headlines.description is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.description, "Ugali, African Prestige meal. Staple food in countries such as Kenya....")

    def test_init_url(self):
        """
        This test case tests if self.news_headlines.url is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.url, "https://www.google.io/img/Africa")

    def test_init_urlToImage(self):
        """
        This test case tests if self.news_headlines.urlToImage is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.urlToImage, "http://www.google.io/img/ugali")

    def test_init_publishedAt(self):
        """
        This test case tests if self.news_headlines.publishedAt is initialized
        properly.
        """
        self.assertEqual(self.news_headlines.publishedAt, "2000-19-03")

import sources
Sources = sources.Sources

class TestSources(unittest.TestCase):
    """
    Test class that defines test cases 
    for the sources class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.

    """

    def setUp(self):
        """
        Set up method to create a new_source instance
        before each test cases.
        """
        self.new_source = Sources("ABC-Z", "News Cast", "https://www.news-cast.com", "Kenya", "We provide in depth news from all around Kenya, with a 5 year experience..."  )

    def tearDown(self):
        self.new_source = None 

    def test_instance(self):
        """
        This method will only assert if self.new_source is an instance of
        Sources class.
        """
        self.assertTrue(isinstance(self.new_source, Sources)) 

    def test_init_id(self):
        """
        This test case tests if self.new_source.id is initialized
        properly.
        """
        self.assertEqual(self.new_source.id, "ABC-Z")

    def test_init_name(self):
        """
        This test case tests if self.new_source.name attribute is initialized
        properly.
        """
        self.assertEqual(self.new_source.name, "News Cast")
    
    def test_init_url(self):
        """
        This test case tests if self.new_source.url property is initialized
        properly.
        """
        self.assertEqual(self.new_source.url, "https://www.news-cast.com")

    def test_init_country(self):
        """
        This test case tests if self.new_source.country property is initialized
        properly.
        """
        self.assertEqual(self.new_source.country, "Kenya")

    def test_init_description(self):
        """
        This test case tests if self.new_source.description property is initialized
        properly.
        """
        self.assertEqual(self.new_source.description, "We provide in depth news from all around Kenya, with a 5 year experience...")
    

if __name__ == "__main__":
    unittest.main()



