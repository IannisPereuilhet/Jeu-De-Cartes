from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.devalement import devalement
from data.attaques.terre.rempart import rempart

def croqueur_de_fruits_verdoyant():
    return Carte(

        nom="CROQUEUR DE FRUITS VERDOYANT",

        numero=17,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            devalement(),
            rempart()
        ],

        passifs=[
            TERRAIN()
        ]
    )