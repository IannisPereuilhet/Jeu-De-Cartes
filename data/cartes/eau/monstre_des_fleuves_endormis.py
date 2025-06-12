from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.fulivert import fulivert
from data.attaques.eau.destru_eau import destru_eau

def monstre_des_fleuves_endormis():
    return Carte(

        nom="MONSTRE DES FLEUVES ENDORMIS",

        numero=120,
        
        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.EAU,

        attaques=[
            fulivert(),
            destru_eau()
        ],

        passifs=None
    )