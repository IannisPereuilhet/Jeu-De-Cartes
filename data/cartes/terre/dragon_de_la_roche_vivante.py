from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.fracture_terrestre import fracture_terrestre

def dragon_de_la_roche_vivante():
    return Carte(

        nom="DRAGON DE LA ROCHE VIVANTE",

        numero=148,

        rarete=TypeRarete.EPIQUE,

        pv=4,#400,

        element=Element.TERRE,

        attaques=[
            fracture_terrestre()
        ],

        passifs=[
            REVANCHE(),

            DISPARITION()
        ]
    )