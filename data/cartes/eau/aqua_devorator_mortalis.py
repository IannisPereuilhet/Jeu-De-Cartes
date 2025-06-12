from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.hasardo import hasardo
from data.attaques.nature.courant_aleatoire import courant_aleatoire

def aqua_devorator_mortalis():
    return Carte(

        nom="AQUA DEVORATOR MORTALIS",

        numero=172,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.EAU,

        attaques=[
            hasardo(),
            courant_aleatoire()
        ],

        passifs=[
            EROSION()
        ]
    )