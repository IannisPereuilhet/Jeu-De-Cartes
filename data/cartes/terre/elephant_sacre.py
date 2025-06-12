from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.plaix_corne import plaix_corne

def elephant_sacre():
    return Carte(

        nom="ELEPHANT SACRE",

        numero=107,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            plaix_corne()
        ],

        passifs=None
    )