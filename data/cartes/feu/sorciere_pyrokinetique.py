from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.flamme_magique import flamme_magique
from data.attaques.lumiere.voile_du_doute import voile_du_doute

def sorciere_pyrokinetique():
    return Carte(

        nom="SORCIERE PYROKINETIQUE",

        numero=51,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.FEU,

        attaques=[
            flamme_magique(),
            voile_du_doute()
        ],

        passifs=None
    )