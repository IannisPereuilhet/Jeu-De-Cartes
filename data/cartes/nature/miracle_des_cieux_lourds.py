from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.poussiere_celeste import poussiere_celeste  
from data.attaques.nature.atterrissage import atterrissage  

def miracle_des_cieux_lourds():
    return Carte(

        nom="MIRACLE DES CIEUX LOURDS",

        numero=147,

        rarete=TypeRarete.EPIQUE,

        pv=450,

        element=Element.NATURE,

        attaques=[
            poussiere_celeste(),
            atterrissage()
        ],

        passifs=None,
    )