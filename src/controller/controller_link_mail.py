from .controller_base import ControllerBase


class ControllerLinkMail(ControllerBase): 
    def __init__(self, model, view):
        super().__init__(model, view)

    def get_mail(self, link_base: str, type_mail: str):
        """Donne l'email contenue dans la balise. 

        Args:
            link_base (str): liens. 
            type_mail (str): html mail

        Returns:
            str: email decoder.
        """

        # type: ignore
        return self.decode_url(link_base.split(type_mail)[1])