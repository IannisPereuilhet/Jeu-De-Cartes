from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.rayon_humide import rayon_humide

def reine_des_ondes():
    return Carte(

        nom="REINE DES ONDES",

        numero=155,

        rarete=TypeRarete.COMMUNE,        

        pv=500,

        element=Element.EAU,

        attaques=[
            rayon_humide()
        ],

        passifs=[
            SOIN_PRIMITIF()
        ]
    )