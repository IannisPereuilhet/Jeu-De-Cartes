from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.transperce_air import transperce_air 

def monarque_des_bois():
    return Carte(

        nom="MONARQUE DES BOIS",

        numero=93,

        rarete=TypeRarete.LEGENDAIRE,

        pv=350,

        element=Element.NATURE,

        attaques=[
            transperce_air()
        ],

        passifs=[
            FUMEE()
        ]
    )