import requests

from bs4 import BeautifulSoup


class ControllerBase:
    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def requests_link(self, url: str):
        r = requests.get(url)
        if r.ok:
            return r
