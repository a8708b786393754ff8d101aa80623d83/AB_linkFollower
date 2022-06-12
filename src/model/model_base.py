import json
import src.model.constant as const

from pathlib import Path


class ModelBase:
    """Classe de base poour les models.

    Attributes:
        data (module): module qui contient toute les constantes.
    """

    def __init__(self):
        """Méthode __init__, initialise l'attribut const au module."""

        self.const = const

    def get_content_data(self, path: str):
        """Donne les données sauvegarder dans le fichier données.
         
        Returns:
            dict: contenue du fichier.
        """

        if Path(path).exists():
            with open(path) as f:
                return json.loads(path)
