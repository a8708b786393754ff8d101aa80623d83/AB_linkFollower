from .view_base import ViewBase

class ViewLinkMail(ViewBase): 
    def __init__(self):
        super().__init__()
        self.mail = 0

    def link_mail(self, link):
        """Méthode pour afficher les liens d'adresse emails de couleur cyan, elle ajoute 1 au compteur d'adresse email.

        Args:
            link (bs4.Element.Tag|str): adresse email.
        """

        self.mail += 1
        print(self.fore.CYAN, link, self.fore.RESET)