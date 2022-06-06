import requests
import re

from bs4 import BeautifulSoup


class ControllerBase:
    def __init__(self, model, view):
        self.model = model()
        self.view = view()
        self.data = {
            'url': None
        }

    def requests_link(self, url: str):
        r = requests.get(url)
        if r.ok:
            self.data['url'] = url  # type: ignore
            return r

    def is_link(self, url: str):
        """Determine si un element est un lien. 
        Args: 
            url(str): lien 

        Returns: 
            bool: True si c'est un lien. False si ce n'est pas un lien
        """
        
        return re.search("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$", url)
