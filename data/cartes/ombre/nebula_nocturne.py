from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.feu_tenebreux import feu_tenebreux

def nebula_nocturne():
    return Carte(

        nom="NEBULA NOCTURNE",

        numero=33,

        rarete=TypeRarete.RARE,

        pv=350,

        element=Element.OMBRE,

        attaques=[
            feu_tenebreux()
        ],

        passifs=[
            ETERNITE(
                valeur=1
            )
        ]
    )