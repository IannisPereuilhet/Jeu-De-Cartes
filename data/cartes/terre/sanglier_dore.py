from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.remue_sol import remue_sol

def sanglier_dore():
    return Carte(

        nom="SANGLIER DORE",

        numero=160,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.TERRE,

        attaques=[
            remue_sol()
        ],

        passifs=[
            SAC_DE_FRAPPE()
        ]
    )