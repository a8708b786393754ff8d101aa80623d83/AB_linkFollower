import json
import re
from .model_base import ModelBase


class ModelLink(ModelBase):
    def __init__(self):
        super().__init__()
        self.path_link_file = self.const.FOLDER_DATA + self.const.FILE_LINK_SAVING

    def save_links(self, data: dict):
        with open(self.path_link_file, 'w') as f:
            json.dump(data, f)

    def is_script(self, content):
        return content.get('type') == 'text/javascript' and content.get(' src') is None 

    def is_link_internal(self, url: str):
        if url.startswith('/'):
            return True

    def get_url_base(self, url):
        try:
            pattern = re.compile(str(url))
        except:
            pass  # trouver quelle erruer extactement
        else:
            for prefix in self.const.ARRAY_CLASSES_HTML:
                # regarde si le pattern(url) contient le prefix
                if not re.match(pattern, prefix):
                    if not url.get(prefix) is None:
                        return url.get(prefix)

