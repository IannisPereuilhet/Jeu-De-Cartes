from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.renaissance_sylvatique import renaissance_sylvatique
from data.attaques.nature.eolienne import eolienne

def girafe_florale():
    return Carte(

        nom="GIRAFE FLORALE",

        numero=72,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.NATURE,

        attaques=[
            renaissance_sylvatique()
        ],

        passifs=[
            SAC_DE_FRAPPE()
        ]
    )