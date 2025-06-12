from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.sucre_doux import sucre_doux

def chenille_mielleuse():
    return Carte(

        nom="CHENILLE MIELLEUSE",

        numero=90,

        rarete=TypeRarete.EPIQUE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            sucre_doux()
        ],

        passifs=[
            TENACITE()
        ]
    )