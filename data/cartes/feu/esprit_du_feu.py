from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.souffle_de_feu import souffle_de_feu
from data.attaques.feu.flambee import flambee

def esprit_du_feu():
    return Carte(

        nom="ESPRIT DU FEU",

        numero=1,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.FEU,

        attaques=[
            souffle_de_feu(),
            flambee()
        ],

        passifs=None
    )