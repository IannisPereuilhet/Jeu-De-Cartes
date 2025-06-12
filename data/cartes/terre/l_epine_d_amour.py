from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.sagesse import sagesse

def l_epine_d_amour():
    return Carte(

        nom="L'EPINE D'AMOUR",

        numero=106,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.TERRE,

        attaques=[
            sagesse()
        ],

        passifs=[
            RENVOI()
        ]
    )