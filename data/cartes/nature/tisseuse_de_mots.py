from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.veuve_noire import veuve_noire

def tisseuse_de_mots():
    return Carte(

        nom="TISSEUSE DE MOTS",

        numero=123,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            veuve_noire()
        ],

        passifs=[
            SAC_DE_FRAPPE()
        ]
    )