import unittest
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


if __name__ == "__main__":
    unittest.main()