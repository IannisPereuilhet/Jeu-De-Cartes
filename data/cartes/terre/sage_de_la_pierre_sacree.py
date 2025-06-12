from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.lance_bouclier import lance_bouclier

def sage_de_la_pierre_sacree():
    return Carte(

        nom="SAGE DE LA PIERRE SACREE",

        numero=16,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.TERRE,

        attaques=[
            lance_bouclier()
        ],

        passifs=[
            VENGEUR()
        ]
    )