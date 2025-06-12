from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.drain_elementaire import drain_elementaire

def cerf_des_couleurs_funebres():
    return Carte(

        nom="CERF DES COULEURS FUNEBRES",

        numero=137,

        rarete=TypeRarete.RARE,

        pv=425,

        element=Element.NATURE,

        attaques=[
            drain_elementaire()
        ],

        passifs=[
            MULTIPLICATEUR()
        ]
    )