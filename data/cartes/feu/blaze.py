from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.feu_humide import feu_humide
from data.attaques.eau.eau_brulante import eau_brulante

def blaze():
    return Carte(

        nom="BLAZE",

        numero=26,

        rarete=TypeRarete.RARE,

        pv=400,

        element=Element.FEU,

        attaques=[
            feu_humide(),
            eau_brulante()
        ],

        passifs=None
    )