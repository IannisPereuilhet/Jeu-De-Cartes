from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.air_pur import air_pur
from data.attaques.nature.courant_aleatoire import courant_aleatoire

def vibrantes_ecailles():
    return Carte(

        nom="VIBRANTES ECAILLES",

        numero=56,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            air_pur(),
            courant_aleatoire()
        ],

        passifs=None
    )