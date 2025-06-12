from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.nuit_finale import nuit_finale
from data.attaques.ombre.tranche_ombre import tranche_ombre
from data.attaques.ombre.tenebr_eal import tenebr_eal

def veilleur_nocturne():
    return Carte(

        nom="VEILLEUR NOCTURNE",

        numero=47,

        rarete=TypeRarete.LEGENDAIRE,

        pv=450,

        element=Element.OMBRE,

        attaques=[
            nuit_finale(),
            tranche_ombre(),
            tenebr_eal()
        ],

        passifs=None
    )