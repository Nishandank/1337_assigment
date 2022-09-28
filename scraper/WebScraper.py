import re

class WebScraper():
    def __init__(self, html) -> None:
        self.html = html

    def get_links(self) -> list:
        regex = r"\s+[^>]*?href=\"([^\"?]*)"

        all_links = re.findall(regex, self.html)
        return all_links
