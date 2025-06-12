from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.rayon_vent import rayon_vent
from data.attaques.lumiere.lumiere_precise import lumiere_precise

def petit_papillon():
    return Carte(

        nom="PETIT PAPILLON",

        numero=13,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            rayon_vent(),
            lumiere_precise()
        ],

        passifs=None
    )