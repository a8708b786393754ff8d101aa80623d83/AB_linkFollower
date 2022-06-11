from .view_base import ViewBase


class ViewLink(ViewBase):
    def __init__(self):
        super().__init__()
        self.internal = 0 
        self.external = 0 
        self.script = 0 
        self.tel = 0 
        self.mail = 0 

    def link_internal(self, link):
        self.internal += 1 
        print(self.fore.RED, link, self.fore.RESET)

    def link_external(self, link):
        self.external += 1
        print(self.fore.BLUE, link, self.fore.RESET)

    def script_javascript(self, script):
        self.script += 1 
        print(self.fore.YELLOW, script, self.fore.RESET)

    def link_tel(self, link_base): 
        self.tel += 1 
        print(self.fore.GREEN, link_base, self.fore.RESET)
        
    def link_mail(self, link): 
        self.mail += 1 
        print(self.fore.CYAN, link, self.fore.RESET)
        
    def stats(self): 
        print(self.back.LIGHTMAGENTA_EX, 
            self.fore.GREEN,'tel:',self.tel,
            self.fore.CYAN,'mail:',self.mail,
            self.fore.YELLOW,'script:',self.script,
            self.fore.RED,'internal:',self.internal, 
            self.fore.BLUE,'external:',self.external
            )