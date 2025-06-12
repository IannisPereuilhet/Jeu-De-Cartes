from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.premiere_valse import premiere_valse
from data.attaques.terre.pietinement import pietinement

def jeunesse_d_aldryn():
    return Carte(

        nom="JEUNESSE D'ALDRYN",

        numero=30,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.NATURE,

        attaques=[
            premiere_valse(),
            pietinement()
        ],

        passifs=[
            RESET()
        ]
    )