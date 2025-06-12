from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.souffle_critique import souffle_critique
from data.attaques.ombre.tranche_ombre import tranche_ombre

def gardien_crepusculaire():
    return Carte(

        nom="GARDIEN CREPUSCULAIRE",

        numero=159,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.NATURE,

        attaques=[
            souffle_critique(),
            tranche_ombre()
        ],

        passifs=None
    )