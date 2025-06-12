from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.arc_en_ciel import arc_en_ciel

def lueur_rousse():
    return Carte(

        nom="LUEUR ROUSSE",

        numero=77,

        rarete=TypeRarete.RARE,

        pv=425,

        element=Element.LUMIERE,

        attaques=[
            arc_en_ciel()
        ],

        passifs=[
            MULTIPLICATEUR()
        ]
    )