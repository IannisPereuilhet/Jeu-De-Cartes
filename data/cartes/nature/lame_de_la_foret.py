from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.pinces import pinces
from data.attaques.nature.soin_critique import soin_critique

def lame_de_la_foret():
    return Carte(

        nom="LAME DE LA FORET",

        numero=103,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.NATURE,

        attaques=[
            pinces(),
            soin_critique()
        ],

        passifs=None
    )