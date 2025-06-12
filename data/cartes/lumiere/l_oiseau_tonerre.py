from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.foudre import foudre
from data.attaques.lumiere.tornade import tornade

def l_oiseau_tonerre():
    return Carte(

        nom="L'OISEAU TONERRE",

        numero=89,

        rarete=TypeRarete.EPIQUE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            foudre(),
            tornade()
        ],

        passifs=None
    )