import json
from .model_base import ModelBase


class ModelLink(ModelBase):
    """Model pour tout ce qui est liens, elle contient toutes les methode pour enregistrez, recuperez, analyser les liens.


    Attributes: 
        path_link_file (str): chemin relatif de fichier ou sont stocker les liens. 

    """

    def __init__(self) -> None:
        super().__init__()
        self.path_link_file = None

    def set_path_link(self, filename: str)->None:
        """Set path link in attribute

        Args:
            filename (str): path file link saving
        """

        self.path_link_file = filename

    def save_links(self, data: dict):
        """Enregistre les liens dans un fichier JSON.

        Args:
            data (dict): données des liens.
        """

        with open(self.path_link_file, 'w') as f:
            json.dump(data, f)

    def is_script(self, link, type_script: list):
        """Méthode qui determine si le lien est un script javascript ou une balise script.

        Args:
            link (_type_): liens 
            type_script (list): array type script

        Returns:
            True| str: True si c'est uen balise script, sinon un lien. 
        """

        if link.name == 'script':
            return True

        return link.get('type') in type_script and link.get('src') is None and link.name == 'script'

    def is_link_internal(self, link: str):
        """Determine si le lien est interne. 
        Args: 
            link(str): lien 

        Returns: 
            bool: True si c'est pas un lien interne.
        """

        return link.startswith('/') or not self.is_link_external(link)

    def is_link_external(self, url: str):
        """Determine si un element est un lien. 
        Args: 
            url(str): lien 

        Returns: 
            bool: True si c'est un lien. False si ce n'est pas un lien
        """

        return re.search('https?:\/\/', str(url))

    def is_tel(self, url: str):
        """Détermine si c'est lien contien un numero de télephone. 

        Args:
            url (str): lien

        Returns:
            bool: True si il contient un numeros de télephone, sinon False 
        """

        return url.startswith('tel:')

    def is_mail(self, url: str):
        """Détermine si c'est lien contien une adresse email. 

        Args:
            url (str): lien

        Returns:
            bool: True si il contient une adresse email, sinon False 
        """

        return url.startswith('mailto:')
