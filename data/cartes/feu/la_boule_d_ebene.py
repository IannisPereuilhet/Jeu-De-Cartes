from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.feu_tenebreux import feu_tenebreux

def la_boule_d_ebene():
    return Carte(

        nom="LA BOULE D'EBENE",

        numero=9,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.FEU,

        attaques=[
            feu_tenebreux()
        ],

        passifs=[
            MYSTERE()
        ]
    )