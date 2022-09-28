from scraper.WebScraper import WebScraper

class TraverseWeb():
    def __init__(self, domain, start_url, include_hashed_urls=False, all_domains=False) -> None:
        self.start_url = start_url
        self.domain = domain
        self.include_hashed_urls = include_hashed_urls
        self.all_domains = all_domains
        self.retrieved_urls = {}
        self.all_parsed_urls = []

    def run(self) -> list:
        self.traverse(self.start_url)
        return self.all_parsed_urls

    def traverse(self, url):
        self.all_parsed_urls.append(url)
        web_scraped = WebScraper.from_request(url, self.domain, self.include_hashed_urls)
        if web_scraped is not None:
            links = web_scraped.get_links()
            full_url_links = [f'{self.domain}{link}' if not link.startswith(
                self.domain) else link for link in links]

            for link in full_url_links:
                if link not in self.all_parsed_urls:
                    self.traverse(link)
            return
