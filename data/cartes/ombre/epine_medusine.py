from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.toxine_enflammee import toxine_enflammee

def epine_medusine():
    return Carte(

        nom="EPINE MEDUSINE",

        numero=178,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            toxine_enflammee()
        ],

        passifs=[
            RESET()
        ]
    )