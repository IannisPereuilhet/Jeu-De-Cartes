from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.souffle_de_terre import souffle_de_terre
from data.attaques.terre.rempart import rempart

def esprit_de_la_terre():
    return Carte(

        nom="ESPRIT DE LA TERRE",

        numero=4,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            souffle_de_terre(),
            rempart()
        ],

        passifs=None
    )