from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.potion_baveuse import potion_baveuse
from data.attaques.ombre.defense_elementaire import defense_elementaire

def chef_croac_croac():
    return Carte(

        nom="CHEF CROAC-CROAC",

        numero=76,

        rarete=TypeRarete.RARE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            potion_baveuse(),
            defense_elementaire()
        ],

        passifs=None
    )