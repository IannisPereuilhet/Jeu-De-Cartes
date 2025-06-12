from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.feu_allie import feu_allie
from data.attaques.feu.embrasement import embrasement

def keria():
    return Carte(

        nom="KERIA",

        numero=117,

        rarete=TypeRarete.RARE,

        pv=425,

        element=Element.FEU,

        attaques=[
            feu_allie(),
            embrasement()
        ],

        passifs=None
    )