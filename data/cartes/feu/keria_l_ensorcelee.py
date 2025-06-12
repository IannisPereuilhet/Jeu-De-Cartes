from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.oriflamme import oriflamme
from data.attaques.feu.embrasement_critique import embrasement_critique

def keria_l_ensorcelee():
    return Carte(

        nom="KERIA L'ENSORCeLEE",

        numero=133,

        rarete=TypeRarete.RARE,

        pv=400,

        element=Element.FEU,

        attaques=[
            oriflamme(),
            embrasement_critique()
        ],

        passifs=None
    )