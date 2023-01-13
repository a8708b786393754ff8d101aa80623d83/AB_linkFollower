from .controller_base import ControllerBase
from bs4 import BeautifulSoup


class ControllerLinkScript(ControllerBase):
    def __init__(self, model, view):
        super().__init__(model, view)

    def get_links_js(self, url: str):
        """Recupere tout les balises de tag script.

        Args:
            url (str): url principale ou seras chercher les liens qui sont dans la page. 

        Returns:
           list: Tableaux des balises javascript.
        """

        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('script')
