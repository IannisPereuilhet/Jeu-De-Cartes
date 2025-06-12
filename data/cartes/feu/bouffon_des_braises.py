from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.feu_sombre import feu_sombre
from data.attaques.feu.feu_tenebreux import feu_tenebreux

def bouffon_des_braises():
    return Carte(

        nom="BOUFFON DES BRAISES",

        numero=49,

        rarete=TypeRarete.COMMUNE,

        pv=350,

        element=Element.FEU,

        attaques=[  
            feu_sombre(),
            feu_tenebreux()
        ],

        passifs=None
    )