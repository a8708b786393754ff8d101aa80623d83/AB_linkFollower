import re
import json
from pathlib import Path


class ModelBase:
    """Classe de base poour les models.

    Attributes:
        data (module): module qui contient toute les constantes.
    """
    def get_url_base(self, link, class_html: list):
        """Méthode qui fait utilise les regex pour voir si on peut recuperer le lien de base. 

        Args:
            link (str| bs4.Element.Tag): lien

        Returns:
            str: lien 
        """

        try:
            pattern = re.compile(str(link))
        except:
            pass  # trouver quelle erruer extactement
        else:
            for prefix in class_html:
                # regarde si le pattern(link) contient le prefix
                if not re.match(pattern, prefix):
                    if not link.get(prefix) is None:
                        return link.get(prefix)
        finally:
            if link.name == 'a':
                return link.get('href')
    
    def get_content_data(self, path: str):
        """Donne les données sauvegarder dans le fichier données.
         
        Returns:
            dict: contenue du fichier.
        """

        if Path(path).exists():
            with open(path) as f:
                return json.loads(path)
