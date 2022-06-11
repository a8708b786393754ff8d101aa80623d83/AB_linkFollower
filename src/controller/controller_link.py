from urllib.parse import unquote
from bs4 import BeautifulSoup

from .controller_base import ControllerBase


class ControllerLink(ControllerBase):
    """Controller pour tout ce qui est liens, elle contient otut les methode pour effectuer des changement sur les liens."""
    
    def __init__(self, model, view):
        super().__init__(model, view)

    def decode_url(self, element: str):
        """Decode les element encode en url.

        Args:
            element (str): element a decoder.

        Returns:
            str: element decoder.
        """
        
        return unquote(element)

    def get_links_css(self, url: str):
        """Recupere tout les balises de tag style.

        Args:
            url (str): url principale ou seras chercher les liens qui sont dans la page.


        Returns:
           list: Tableaux des balises css.
        """
        
        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('link', {'rel': 'stylesheet'})

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

    def get_links_img(self, url: str):
        """Recupere tout les balises de tag img.

        Args:
            url (str): url principale ou seras chercher les liens qui sont dans la page. 


        Returns:
           list: Tableaux des balises image.
        """
        
        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('img')

    def get_links_tag_a(self, url: str):
        """Recupere tout les balises de tag a. 

        Args:
            url (str): url principale ou seras chercher les liens qui sont dans la page. 


        Returns:
           list: Tableaux des balises liens.
        """
        
        resp = self.requests_link(url)
        if not resp is None:
            return BeautifulSoup(resp.text, 'lxml').find_all('a')

    def get_links(self, url: str):
        """Donne tout les types de liens.

        Args:
            url (str): url principale ou seras chercher les liens qui sont dans la page. 

        Returns:
            dict: Tableaux d'urls avec la clef.
        """

        data = {
            'css': None,
            'img': None,
            'js': None,
            'a': None
        }

        data['css'] = self.get_links_css(url)  # type: ignore
        data['img'] = self.get_links_img(url)  # type: ignore
        data['js'] = self.get_links_js(url)  # type: ignore
        data['a'] = self.get_links_tag_a(url)  # type: ignore

        return data

    def get_mail(self, link_base: str):
        """Donne l'email contenue dans la balise. 

        Args:
            link_base (str): liens. 

        Returns:
            str: email decoder.
        """

        # type: ignore
        return self.decode_url(link_base.split(self.model.const.ARRAY_TYPE_INFORMATION_HTML[1])[1])

    def get_tel(self, link_base: str):
        """Donne le numero de téléphone contenue dans la balise. 

        Args:
            link_base (str): liens. 

        Returns:
            str: numeros de telephone decoder.
        """

        # type: ignore
        return self.decode_url(link_base.split(self.model.const.ARRAY_TYPE_INFORMATION_HTML[0])[1])
