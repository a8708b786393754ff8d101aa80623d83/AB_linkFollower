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
        print(
            self.back.LIGHTBLACK_EX, 
            self.fore.WHITE,'tel:',self.tel,
            'mail:',self.mail,
            'script:',self.script,
            'internal:',self.internal, 
            'external:',self.external, 
            self.fore.RESET,
            self.back.RESET
            )