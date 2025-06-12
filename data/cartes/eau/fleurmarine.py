from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.nageoire_sifflante import nageoire_sifflante
from data.attaques.eau.fond_marin import fond_marin

def fleurmarine():
    return Carte(

        nom="FLEURMARINE",

        numero=119,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.EAU,

        attaques=[
            nageoire_sifflante(),
            fond_marin()
        ],

        passifs=None
    )