from .view_base import ViewBase


class ViewLink(ViewBase):
    def __init__(self):
        super().__init__()

    def link_internal(self, link):
        print(self.fore.RED, link, self.fore.RESET)

    def link_external(self, link):
        print(self.fore.BLUE, link, self.fore.RESET)

    def script_javascript(self, script):
        print(self.fore.YELLOW, script, self.fore.RESET)
