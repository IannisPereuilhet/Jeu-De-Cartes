from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.sol_enflamme import sol_enflamme
from data.attaques.terre.etranglement import etranglement

def gardien_des_entrees():
    return Carte(

        nom="GARDIEN DES ENTREES",

        numero=125,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.TERRE,

        attaques=[
            sol_enflamme(),
            etranglement()
        ],

        passifs=None
    )