from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.rayon_vent import rayon_vent
from data.attaques.nature.bond_rapide import bond_rapide

def mante_des_contrees():
    return Carte(

        nom="MANTE DES CONTREES",

        numero=57,

        rarete=TypeRarete.COMMUNE,

        pv=325,

        element=Element.NATURE,

        attaques=[
            rayon_vent(),
            bond_rapide()
        ],

        passifs=None
    )