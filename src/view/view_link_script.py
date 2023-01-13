from .view_base import ViewBase

class ViewLinkScript(ViewBase): 
    def __init__(self):
        super().__init__()

    def script_javascript(self, script):
        """Méthode pour afficher les script javascript de couleur jaune, elle ajoute 1 au compteur de script.

        Args:
            script (bs4.Element.Tag|str): lien/script javascript.
        """

        self.script += 1
        print(self.fore.YELLOW, script, self.fore.RESET)
