from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.murmure import murmure

def murmures_du_corail_noir():
    return Carte(

        nom="MURMURES DU CORAIL NOIR",

        numero=102,

        rarete=TypeRarete.COMMUNE,        

        pv=500,

        element=Element.EAU,

        attaques=[
            murmure()
        ],

        passifs=[
            MULTIPLICATEUR()
        ]
    )