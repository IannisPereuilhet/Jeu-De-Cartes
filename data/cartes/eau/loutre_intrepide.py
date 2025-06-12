from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.morsure import morsure

def loutre_intrepide():
    return Carte(

        nom="LOUTRE INTREPIDE",

        numero=54,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.EAU,

        attaques=[
            morsure()
        ],

        passifs=None
    )