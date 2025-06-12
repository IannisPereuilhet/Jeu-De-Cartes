from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.ecailles import ecailles

def ecaille():
    return Carte(

        nom="ECAILLE",

        numero=108,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.TERRE,

        attaques=[
            ecailles()
        ],

        passifs=[
            REVANCHE()
        ]
    )