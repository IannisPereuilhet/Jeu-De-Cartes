from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.marecage import marecage

def batracien_des_marais():
    return Carte(

        nom="BATRACIEN DES MARAIS",

        numero=52,

        rarete=TypeRarete.COMMUNE,

        pv=475,

        element=Element.EAU,

        attaques=[
            marecage()
        ],

        passifs=[
            RENVOI()
        ]
    )