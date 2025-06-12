from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.tenebr_eal import tenebr_eal

def essence_spectrale():
    return Carte(

        nom="ESSENCE SPECTRALE",

        numero=63,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.OMBRE,

        attaques=[
            tenebr_eal()
        ],

        passifs=[
            TERRAIN(),
            SOIN_PRIMITIF()
        ]
    )