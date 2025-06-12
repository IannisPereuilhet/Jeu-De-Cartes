from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.roule_boule import roule_boule

def pangolin_des_prairies():
    return Carte(

        nom="PANGOLIN DES PRAIRIES",

        numero=60,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.TERRE,

        attaques=[
            roule_boule()
        ],

        passifs=None
    )