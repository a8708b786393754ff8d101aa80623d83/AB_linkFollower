from .model_base import ModelBase

class ModelLinkScript(ModelBase): 
    def __init__(self) -> None:
        super().__init__()

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
    