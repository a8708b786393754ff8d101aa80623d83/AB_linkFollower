import json
import src.model.constant as const

from pathlib import Path


class ModelBase:
    """Classe model de base, cette classe sera heriter des enfants model."""

    def __init__(self):
        self.const = const

    def get_content_data(self, path: str):
        """Donne les données sauvegarder dans le fichier données 
        Returns:
            dict: contenue du fichier 
        """

        if Path(path).exists():
            with open(path) as f:
                return json.loads(path)
