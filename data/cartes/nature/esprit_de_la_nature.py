from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.souffle_d_air import souffle_d_air
from data.attaques.nature.eolienne import eolienne

def esprit_de_la_nature():
    return Carte(

        nom="ESPRIT DE LA NATURE",

        numero=3,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            souffle_d_air(),
            eolienne()
        ],

        passifs=None
    )