from .model_base import ModelBase

class ModeLinkEmail(ModelBase): 
    def __init__(self) -> None:
        super().__init__()


    def is_mail(self, url: str):
        """Détermine si c'est lien contien une adresse email. 

        Args:
            url (str): lien

        Returns:
            bool: True si il contient une adresse email, sinon False 
        """

        return url.startswith('mailto:')