from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.brute_flamme import brute_flamme
from data.attaques.terre.devalement import devalement

def colosse_igne():
    return Carte(

        nom="COLOSSE IGNE",

        numero=7,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.FEU,

        attaques=[
            brute_flamme(),
            devalement()
        ],

        passifs=None
    )