import requests


class ControllerBase:
    def __init__(self, model, view):
        self.model = model()
        self.view = view()
        self.data = {
            'url': None
        }

    def requests_link(self, url: str):
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            return None
        else:
            if r.ok:
                self.data['url'] = url  # type: ignore
                return r