from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.haleau import haleau
from data.attaques.eau.soin_d_eau import soin_d_eau

def float_cristallin():
    return Carte(

        nom="FLOT CRISTALLIN",

        numero=12,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.EAU,

        attaques=[
            haleau(),
            soin_d_eau()
        ],

        passifs=None
    )