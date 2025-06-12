from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.destru_flamme import destru_flamme

def flamboyant_des_cavernes():
    return Carte(

        nom="FLAMBOYANT DES CAVERNES",

        numero=99,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.FEU,

        attaques=[
            destru_flamme()
        ],

        passifs=[
            TERRAIN()
        ]
    )