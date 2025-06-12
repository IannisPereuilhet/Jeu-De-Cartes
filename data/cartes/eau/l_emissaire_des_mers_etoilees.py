from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.turbo_splash import turbo_splash

def l_emissaire_des_mers_etoilees():
    return Carte(

        nom="L'EMISSAIRE DES MERS ETOILEES",

        numero=10,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.EAU,

        attaques=[
            turbo_splash()
        ],

        passifs=[
            TERRAIN()
        ]
    )