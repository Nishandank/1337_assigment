import unittest
from scraper.WebScraper import WebScraper
from scraper.TraverseWeb import TraverseWeb
from pathlib import Path


class TestHtmlRegex(unittest.TestCase):
    def test_regex(self):
        html = read_file('web1.html')
        web_scraper = WebScraper(
            html=html, domain='localhost', include_hashed_url=False, all_domains=False)
        self.assertEqual(web_scraper.get_links(), [
                         '/css/styles.css', '/testlinkworks'])


class TestTraverse(unittest.TestCase):
    def test_traverse(self):
        traverse_web = TraverseWeb(
            domain='https://1337.tech', start_url='https://1337.tech', include_hashed_urls=True)
        all_urls = traverse_web.run()
        self.assertEqual(len(all_urls),13 )


def read_file(name):
    path = Path(__file__).parent / name
    if path.exists():
        with open(path, 'r') as f:
            data = f.read()
            return data
    return None


unittest.main()
