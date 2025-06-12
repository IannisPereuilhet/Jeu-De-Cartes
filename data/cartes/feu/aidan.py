from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.chanceur import chanceur
from data.attaques.feu.paie_torche import paie_torche

def aidan():
    return Carte(

        nom="AIDAN",

        numero=115,

        rarete=TypeRarete.COMMUNE,

        pv=350,

        element=Element.FEU,

        attaques=[
            chanceur(),
            paie_torche()
        ],

        passifs=None
    )