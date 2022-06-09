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
        return content.get('type') == 'text/javascript'
    