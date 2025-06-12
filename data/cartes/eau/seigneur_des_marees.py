from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.missile_terre_eau import missile_terre_eau

def seigneur_des_marees():
    return Carte(

        nom="SEIGNEUR DES MAREES",

        numero=135,

        rarete=TypeRarete.RARE,        

        pv=450,

        element=Element.EAU,

        attaques=[
            missile_terre_eau()
        ],

        passifs=[
            SAC_DE_FRAPPE(),
            FUMEE()
        ],
    )