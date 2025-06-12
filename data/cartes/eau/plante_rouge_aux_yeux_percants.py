from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.etreinte_florale import etreinte_florale

def plante_rouge_aux_yeux_percants():
    return Carte(

        nom="PLANTE ROUGE AUX YEUX PERCANTS",

        numero=154,

        rarete=TypeRarete.COMMUNE,        

        pv=450,

        element=Element.EAU,

        attaques=[
            etreinte_florale()
        ],

        passifs=None
    )