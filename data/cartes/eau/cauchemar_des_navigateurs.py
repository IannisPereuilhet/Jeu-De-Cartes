from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.croc_terre import croc_terre
from data.attaques.nature.croc_d_air import croc_d_air
from data.attaques.eau.croc_d_eau import croc_d_eau

def cauchemar_des_navigateurs():
    return Carte(

        nom="CAUCHEMAR DES NAVIGATEURS",

        numero=183,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.EAU,

        attaques=[
            croc_terre(),
            croc_d_air(),
            croc_d_eau()
        ],

        passifs=None
    )