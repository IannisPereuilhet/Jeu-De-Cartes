from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.torche import torche
from data.attaques.feu.doux_foyer import doux_foyer

def sbire_des_flammes():
    return Carte(

        nom="SBIRE DES FLAMMES",

        numero=151,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.FEU,

        attaques=[
            torche(),
            doux_foyer()
        ],

        passifs=None
    )