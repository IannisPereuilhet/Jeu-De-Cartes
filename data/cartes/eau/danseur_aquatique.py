from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.aspireau import aspireau

def danseur_aquatique():
    return Carte(

        nom="DANSEUR AQUATIQUE",

        numero=53,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.EAU,

        attaques=[
            aspireau()
        ],

        passifs=[
            TERRAIN()
        ]
    )