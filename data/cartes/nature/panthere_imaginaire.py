from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.vitesse_folle import vitesse_folle

def panthere_imaginaire():
    return Carte(

        nom="PANTHERE IMAGINAIRE",

        numero=83,

        rarete=TypeRarete.EPIQUE,

        pv=300,

        element=Element.NATURE,

        attaques=[
            vitesse_folle()
        ],

        passifs=None
    )