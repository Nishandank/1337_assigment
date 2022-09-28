import re

class WebScraper():
    def __init__(self, html, domain, include_hashed_url, all_domains=False) -> None:
        self.html = html
        self.domain = domain
        self.include_hashed_url = include_hashed_url
        self.all_domains = all_domains


    def get_links(self) -> list:
        regex = r"\s+[^>]*?href=\"([^\"?]*)"

        all_links = re.findall(regex, self.html)
        # Filter links to remove root and hashed links
        if not self.include_hashed_url:
            filtered_links = [
                link for link in all_links if link != '/' and '#' not in link]
        else:
            filtered_links = [link for link in all_links if link != '/']

        if not self.all_domains:
            filtered_links = [link for link in filtered_links if link.startswith(
                '/') or link.startswith(self.domain)]

        return filtered_links
