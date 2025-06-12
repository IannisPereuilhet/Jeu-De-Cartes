from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.explosion import explosion

def prisonniere_de_la_machine():
    return Carte(

        nom="PRISONNIERE DE LA MACHINE",

        numero=116,

        rarete=TypeRarete.COMMUNE,

        pv=300,

        element=Element.FEU,

        attaques=[
            explosion()
        ],

        passifs=None
    )