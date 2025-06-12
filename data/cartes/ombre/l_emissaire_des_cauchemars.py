from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.flammes_cosmiques import flammes_cosmiques
from data.attaques.ombre.lumiere_cosmique import lumiere_cosmique

def l_emissaire_des_cauchemars():
    return Carte(

        nom="L'EMISSAIRE DES CAUCHEMARS",

        numero=142,

        rarete=TypeRarete.RARE,

        pv=500,

        element=Element.OMBRE,

        attaques=[
            flammes_cosmiques(),
            lumiere_cosmique()
        ],

        passifs=[
            MULTIPLICATEUR()
        ]
    )