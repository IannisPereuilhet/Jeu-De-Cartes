from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.profondeurs import profondeurs
from data.attaques.eau.boost_abyssal import boost_abyssal

def titan_des_eaux_brillantes():
    return Carte(

        nom="TITAN DES EAUX BRILLANTES",

        numero=118,

        rarete=TypeRarete.COMMUNE,        

        pv=450,

        element=Element.EAU,

        attaques=[
            profondeurs(),
            boost_abyssal()
        ],

        passifs=None,
    )