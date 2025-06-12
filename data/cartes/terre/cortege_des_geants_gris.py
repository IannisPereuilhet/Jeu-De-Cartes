from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.souffle_lent import souffle_lent
from data.attaques.terre.prehistopic import prehistopic
from data.attaques.terre.avalement import avalement

def cortege_des_geants_gris():
    return Carte(

        nom="CORTEGE DES GEANTS GRIS",

        numero=175,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            souffle_lent(),
            prehistopic(),
            avalement()
        ],

        passifs=None
    )