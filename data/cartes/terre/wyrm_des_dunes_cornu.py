from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.morsure_brulante import morsure_brulante

def wyrm_des_dunes_cornu():
    return Carte(

        nom="WYRM DES DUNES CORNU",

        numero=124,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.TERRE,

        attaques=[
            morsure_brulante()
        ],

        passifs=[
            TERRAIN(),
            MULTIPLICATEUR()
        ]
    )