from .controller_base import ControllerBase


class ControllerLinkTel(ControllerBase):
    def __init__(self, model, view):
        super().__init__(model, view)

    def get_tel(self, link_base: str, type_tel: str):
        """Donne le numero de téléphone contenue dans la balise. 

        Args:
            link_base (str): liens. 
            type_tel (str): html tel

        Returns:
            str: numeros de telephone decoder.
        """

        # type: ignore
        return self.decode_url(link_base.split(type_tel)[1])
