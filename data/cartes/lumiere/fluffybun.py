from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.bond_lumineux import bond_lumineux
from data.attaques.lumiere.pelage_printanier import pelage_printanier

def fluffybun():
    return Carte(

        nom="FLUFFYBUN",

        numero=168,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.LUMIERE,

        attaques=[
            bond_lumineux(),
            pelage_printanier()
        ],

        passifs=None
    )