from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.avaleau import avaleau

def blancheur_aquatique():
    return Carte(

        nom="BLANCHEUR AQUATIQUE",

        numero=100,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.EAU,

        attaques=[
            avaleau()
        ],

        passifs=None
    )