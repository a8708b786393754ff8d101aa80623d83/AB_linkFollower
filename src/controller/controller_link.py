import requests
from bs4 import BeautifulSoup

from .controller_base import ControllerBase


class ControllerLink(ControllerBase):
    def __init__(self, model, view):
        super().__init__(model, view)

    def get_links_css(self, url: str):
        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('link', {'rel': 'stylesheet'})

    def get_links_js(self, url: str):
        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('script')

    def get_links_img(self, url: str):
        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('img')

    def get_links_tag_a(self, url: str):
        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('a')

        """faire une methode qui identifie a qui appartient les liens 
        """

    def get_links(self, url: str):
        data = []
        data.append(self.get_links_css(url))
        data.append(self.get_links_img(url))
        data.append(self.get_links_js(url))
        data.append(self.get_links_tag_a(url))
        
        return data
