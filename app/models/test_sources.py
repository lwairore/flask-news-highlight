import unittest
import sources
Sources = sources.Sources

class TestSources(unittest.TestCase):
    """
    Text class that defines test cases 
    for the sources class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.

    """

    def setUp(self):
        """
        Set up method to create a new_source instance
        before each test cases.
        """
        self.new_source = Sources("ABC-Z", "News Cast", "https://www.news-cast.com ", "Kenya", "We provide in depth news from all around Kenya, with a 5 year experience..."  )

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

if __name__ == "__main__":
    unittest.main()