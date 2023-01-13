from .view_base import ViewBase


class ViewLink(ViewBase):
    """Vue liées au liens, elle affiche tout les liens(interne, externe, javascript, etc...), elle herite de la vue de base(ViewBase).

    Attributes:
        internal (int): nombre de lien interne.
        external (int): nombre de lien externe.
        script (int): nombre de script javascript.
        tel (int): nombre de lien de telephone.
        mail (int): nombre de lien contenant une adresse email.
    """

    def __init__(self):
        """Méthode __init__, elle initialise tout ces attributs a zeros."""

        super().__init__()
        self.internal = 0
        self.external = 0

    def link_internal(self, link):
        """Méthode pour afficher les liens interne de couleur rouge, elle ajoute 1 au compteur de lien interne.

        Args:
            link (bs4.Element.Tag|str): lien interne.
        """

        self.internal += 1
        print(self.fore.RED, link, self.fore.RESET)

    def link_external(self, link):
        """Méthode pour afficher les liens etxerne de couleur bleu, elle ajoute 1 au compteur de lien externe.

        Args:
            link (bs4.Element.Tag|str): lien externe.
        """

        self.external += 1
        print(self.fore.BLUE, link, self.fore.RESET)

    def stats(self):
        """Affiche les statistiques, affcihe le nombre de compteur avec de couleur de fond gris est le texte ne blanc."""

        print(
            self.back.LIGHTBLACK_EX,
            self.fore.WHITE, 'tel:', self.tel,
            'mail:', self.mail,
            'script:', self.script,
            'internal:', self.internal,
            'external:', self.external,
            self.fore.RESET,
            self.back.RESET
        )
