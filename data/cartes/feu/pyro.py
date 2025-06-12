from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.poing_flamme import poing_flamme

def pyro():
    return Carte(

        nom="PYRO",

        numero=97,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.FEU,

        attaques=[
            poing_flamme()
        ],

        passifs=None
    )