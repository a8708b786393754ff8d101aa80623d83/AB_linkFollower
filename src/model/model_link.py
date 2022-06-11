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
        if content.name == 'script':
            return True

        return content.get('type') in self.const.ARRAY_TYPE_SCRIPT and content.get('src') is None and content.name == 'script'

    def is_link_internal(self, url: str):
        return url.startswith('/') or not self.is_link_external(url)

    def is_link_external(self, url: str):
        """Determine si un element est un lien. 
        Args: 
            url(str): lien 

        Returns: 
            bool: True si c'est un lien. False si ce n'est pas un lien
        """

        return re.search('https?:\/\/', str(url))

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
        finally:
            if url.name == 'a':
                return url.get('href')
