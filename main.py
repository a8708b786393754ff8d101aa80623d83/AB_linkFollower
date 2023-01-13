#! /usr/bin/python3
from src.controller import controller_link as c
from src.model import model_link as m
from src.view import view_link as v

import constant as const

url = 'https://www.youtube.com/watch?v=0D7WSDugT6g'

controller = c.ControllerLink(m.ModelLink, v.ViewBase)
controller.model.set_path_link(const.FOLDER_DATA + const.FILE_LINK_SAVING)

view = v.ViewLink()

if not controller.requests_link(url) is None:
    for keys, links in controller.get_links(url).items():
        for link in links:  # type: ignore
            if controller.model.is_script(link, const.ARRAY_TYPE_SCRIPT):
                view.script_javascript(link)
            else:
                link_base = controller.model.get_url_base(link, const.ARRAY_CLASSES_HTML)

                if controller.model.is_tel(link_base):
                    view.link_tel(controller.get_tel(link_base, const.HTML_TEL))
                    
                elif controller.model.is_mail(link_base):
                    view.link_mail(controller.get_mail(link_base, const.HTML_MAIL))

                elif controller.model.is_link_internal(link_base):
                    view.link_internal(link_base)

                elif not controller.model.is_link_external(link_base) is None:
                    view.link_external(link_base)

view.stats()
