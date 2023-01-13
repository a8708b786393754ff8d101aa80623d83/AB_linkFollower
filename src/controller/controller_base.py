from urllib.parse import unquote
import requests


class ControllerBase:
    """Classe de base poour les controllers.

    Attributes:
        model (obj): Classe Model pour accder au données  
        view (obj):  Classe View pour utiliser ses méthode
        data (dict): données qui stocke les liens .
    """

    def __init__(self, model, view):
        """Methode __init__.

        Args:
            model (obj): classe model
            view (obj): classe view
        """

        self.model = model()
        self.view = view()
        self.data = {
            'url': None
        }

    def requests_link(self, url: str):
        """Execute une requete HTTP

        Args:
            url (str): lien pour executer la requete 

        Returns:
            None si l'url ne renvoie pas de reponse, requests.Response
        """

        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            return None
        else:
            if r.ok:
                self.data['url'] = url  # type: ignore
                return r

    def decode_url(self, element: str):
        """Decode les element encode en url.

        Args:
            element (str): element a decoder.

        Returns:
            str: element decoder.
        """

        return unquote(element)
