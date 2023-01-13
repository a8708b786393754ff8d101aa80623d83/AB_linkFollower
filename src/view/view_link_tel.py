from .view_base import ViewBase

class ViewLinkTel(ViewBase):
    def __init__(self):
        super().__init__()
        self.tel = 0


    def link_tel(self, link_base):
        """Méthode pour afficher les liens de numero de telephone de couleur vert, elle ajoute 1 au compteur de lien numero de telephone.

        Args:
            link_base (bs4.Element.Tag|str): lien de numero de telephone.
        """

        self.tel += 1
        print(self.fore.GREEN, link_base, self.fore.RESET)