from colorama import Fore, Back


class ViewBase:
    """Classe de base poour les vue.

    Attributes:
        fore (obj): objet qui change les couleur de texte
        back (obj): objet qui change les couleur du fond
    """

    def __init__(self):
        """Méthode __init__, initialise les attribut au classe."""

        self.fore = Fore
        self.back = Back
