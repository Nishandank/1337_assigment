import re
import requests
from scraper.Utils import Utils

class WebScraper():
    def __init__(self, html, domain, include_hashed_url, all_domains=False) -> None:
        self.html = html
        self.domain = domain
        self.include_hashed_url = include_hashed_url
        self.all_domains = all_domains

    @classmethod
    def from_raw_response(cls, raw_html, base_path, include_hashed_url):
        return cls(html=raw_html, base_path=base_path, include_hashed_url=include_hashed_url)

    @classmethod
    def from_request(cls, url, domain, include_hashed_url, all_domains=False):
        try:
            # incase the url contains . at the end like /css/app.css then we dont parse as it
            if Utils.is_html(url):
                response = requests.get(url)
                if response.ok:
                    return cls(html=response.text, domain=domain, include_hashed_url=include_hashed_url, 
                    all_domains=all_domains)
                else:
                    raise Exception(f"bad response code from url: {url}")
            else:
                return None
        except Exception as e:
            return None

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
