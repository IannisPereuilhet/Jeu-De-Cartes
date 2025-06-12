from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.double_souffle import double_souffle
from data.attaques.nature.bond_rapide import bond_rapide

def sylvan_protecteur_de_la_verdure():
    return Carte(

        nom="SYLVAIN, PROTECTEUR DE LA VERDURE",

        numero=39,

        rarete=TypeRarete.EPIQUE,

        pv=450,

        element=Element.NATURE,

        attaques=[
            double_souffle(),
            bond_rapide()
        ],

        passifs=[
            EROSION()
        ]
    )