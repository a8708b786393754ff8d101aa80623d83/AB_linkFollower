import json
import src.model.constant as const

from pathlib import Path


class ModelBase:
    """Classe model de base, cette classe sera heriter des enfants model."""

    def __init__(self):
        self.const = const
        self.path_link_file = self.const.FOLDER_DATA + self.const.FILE_LINK_SAVING

    def get_content_data(self):
        """Donne les données sauvegarder dans le fichiers des liens 
        Returns:
            dict: contenue du fichier 
        """

        if Path(self.path_link_file).exists():
            with open(self.path_link_file) as f:
                return json.loads(self.path_link_file)

