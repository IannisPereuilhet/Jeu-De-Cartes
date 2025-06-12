from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.chaos_elementaire import chaos_elementaire

def cameleon_arc_en_ciel():
    return Carte(

        nom="CAMELEON ARC-EN-CIEL",

        numero=55,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            chaos_elementaire()
        ],

        passifs=[
            CIMETIERE()
        ]
    )