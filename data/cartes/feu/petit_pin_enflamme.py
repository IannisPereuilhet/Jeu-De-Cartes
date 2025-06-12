from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.feu_de_bois import feu_de_bois

def petit_pin_enflamme():
    return Carte(

        nom="PETIT PIN ENFLAMME",

        numero=98,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.FEU,

        attaques=[
            feu_de_bois()
        ],

        passifs=[
            POISON()
        ]
    )