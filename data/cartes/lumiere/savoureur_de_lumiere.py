from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.eclat import eclat
from data.attaques.lumiere.ecran import ecran

def savoureur_de_lumiere():
    return Carte(

        nom="SAVOUREUR DE LUMIERE",

        numero=114,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            eclat(),
            ecran()
        ],

        passifs=[
            TERRAIN()
        ]
    )