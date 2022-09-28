import unittest
from scraper.WebScraper import  WebScraper 
from pathlib import Path


class TestHtmlRegex(unittest.TestCase):
    def test_regex(self):
        html = read_file('web1.html')
        web_scraper = WebScraper(html=html)
        self.assertEqual(web_scraper.get_links(),['/css/styles.css', 'testlink', '/testlinkworks'])
        


def read_file(name):
    path = Path(__file__).parent / name
    if path.exists():
        with open(path, 'r') as f:
            data = f.read()
            return data
    return None


unittest.main()
