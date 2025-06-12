from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.resistance_nordique import resistance_nordique
from data.attaques.terre.empal_soin import empal_soin

def gardien_des_pics():
    return Carte(

        nom="GARDIEN DES PICS",

        numero=74,

        rarete=TypeRarete.RARE,

        pv=500,

        element=Element.TERRE,

        attaques=[
            resistance_nordique(),
            empal_soin()
        ],

        passifs=None
    )