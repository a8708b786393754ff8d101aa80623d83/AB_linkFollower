import json 
from .model_base import ModelBase


class ModelLink(ModelBase):
    def __init__(self):
        self.path_link_file = self.const.FOLDER_DATA + self.const.FILE_LINK_SAVING
        super().__init__()

    def save_links(self, data: dict):
        with open(self.path_link_file, 'w') as f:
            json.dump(data, f)