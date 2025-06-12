from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.hasardo import hasardo
from data.attaques.lumiere.phare import phare

def luminaire_abyssal():
    return Carte(

        nom="LUMINAIRE ABYSSAL",

        numero=81,
        
        rarete=TypeRarete.EPIQUE,

        pv=375,

        element=Element.EAU,

        attaques=[
            hasardo(),
            phare()
        ],

        passifs=None
    )