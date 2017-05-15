import unittest
from mock import MagicMock

from spiders.bbc import BbcSpider

class TestScrapy(unittest.TestCase):
    def article_test(self):
        mock_cursor = ["someitem"]
        mock_db = MagicMock()
        mock_db.articles = MagicMock()
        mock_db.articles.find = MagicMock(return_value=mock_cursor)
        some_url = "http://www.bbc.com"

        result = BbcSpider(some_url)

        self.assertEqual(result, ["someitem"])
        mock_db.articles.find.assert_called_with({"url": some_url})

if __name__ == '__main__':
    unittest.main()