from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.tsunami import tsunami

def cauda_regalis():
    return Carte(

        nom="CAUDA REGALIS",

        numero=28,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.EAU,

        attaques=[
            tsunami()
        ],

        passifs=[
            POISON()
        ]
    )