from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.soin_d_air import soin_d_air
from data.attaques.eau.soin_d_eau import soin_d_eau
from data.attaques.lumiere.soin_de_lumiere import soin_de_lumiere

def fille_des_bois():
    return Carte(

        nom="FILLE DES BOIS",

        numero=15,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.NATURE,

        attaques=[
            soin_d_air(),
            soin_d_eau(),
            soin_de_lumiere()
        ],

        passifs=None
    )