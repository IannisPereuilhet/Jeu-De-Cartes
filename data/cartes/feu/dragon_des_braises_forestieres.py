from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.souffle_du_dragon import souffle_du_dragon

def dragon_des_braises_forestieres():
    return Carte(

        nom="DRAGON DES BRAISES FORESTIERES",

        numero=152,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.FEU,

        attaques=[
            souffle_du_dragon()
        ],

        passifs=[
            FUMEE(),

            IMMUNITE()
        ]
    )