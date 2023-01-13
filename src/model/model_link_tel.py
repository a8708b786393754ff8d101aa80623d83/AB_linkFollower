from .model_link import ModelLink

class ModelLinkTel(ModelLink): 
    def __init__(self) -> None:
        super().__init__()

    def is_tel(self, url: str):
        """Détermine si c'est lien contien un numero de télephone. 

        Args:
            url (str): lien

        Returns:
            bool: True si il contient un numeros de télephone, sinon False 
        """

        return url.startswith('tel:')