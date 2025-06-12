from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.supra_rayon_humide import supra_rayon_humide

def hyppocampe_nimbe():
    return Carte(

        nom="HYPPOCAMPE NIMBE",

        numero=27,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.EAU,

        attaques=[
            supra_rayon_humide()
        ],

        passifs=[
            RESET()
        ]
    )