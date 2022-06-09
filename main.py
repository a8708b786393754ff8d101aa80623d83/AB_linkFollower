#! /usr/local/bin/python3.10
from src.controller import controller_link as c
from src.model import model_link as m
from src.view import view_base as v

"""
    FAIRE UN SCRIPT QUI SUIS UN LIEN EST QUI SUIS LES LIEN QUI EST DANS LE LIEN
    TOUT CA C'EST RECURSIF, EN MVC
    LES LIENS SONT ENREGISTREZ DANS UN FICHIER EN JSON
    LES CLEF C'EST LE SITE QUI CONTIENT LE LIEN EST SONT LIEN 
    
    1: lui donner un lien
    2: il liste tout les liens qui sont dans la page 
    3: il identifie les liens qui appartient a cette page
    4: il parcour les liens est ainsi de suite 
"""
url = 'https://ecurie-des-4-chemins.fr/'

controller = c.ControllerLink(m.ModelLink, v.ViewBase)

if not controller.requests_link(url) is None:
    for keys, links in controller.get_links(url).items(): 
        for link in links: # type: ignore
            if not controller.model.is_script(link): # si c'est pas un script javascript 
                controller.model.get_url_base(link)
            else: # si c'est un lien 
                print(link)
