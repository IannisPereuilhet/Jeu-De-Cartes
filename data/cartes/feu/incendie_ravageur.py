from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.incendie import incendie

def incendie_ravageur():
    return Carte(

        nom="INCENDIE RAVAGEUR",

        numero=50,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.FEU,

        attaques=[
            incendie()
        ],

        passifs=None
    )