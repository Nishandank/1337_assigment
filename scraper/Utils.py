

class Utils():

    @staticmethod
    def is_html(url) -> bool:
        url_split = url.replace('https://','').split('/')
        if len(url_split) > 1:
            return not '.' in url_split[len(url_split) - 1]
        return True

    @staticmethod
    def is_hashed(url) -> bool:
        url_split = url.replace('https://','').split('/')
        if len(url_split) > 1:
            return url_split[len(url_split)-1].startswith('#')
        return False