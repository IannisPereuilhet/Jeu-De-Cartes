from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.bond_noir import bond_noir

def demon_miaulant():
    return Carte(

        nom="DEMON MIAULANT",

        numero=109,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            bond_noir()
        ],

        passifs=None
    )