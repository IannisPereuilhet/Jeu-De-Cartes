from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.amitie import amitie
from data.attaques.nature.amour import amour

def maitresse_de_la_girafe_pourpre():
    return Carte(

        nom="MAITRESSE DE LA GIRAFE POURPRE",

        numero=138,

        rarete=TypeRarete.RARE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            amitie(),
            amour()
        ],

        passifs=[
            VENGEUR()
        ]
    )