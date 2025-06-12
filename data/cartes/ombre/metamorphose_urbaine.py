from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.griffe_ombre import griffe_ombre

def metamorphose_urbaine():
    return Carte(

        nom="METAMORPHOSE URBAINE",

        rarete=TypeRarete.RARE,

        numero=75,

        pv=450,

        element=Element.OMBRE,

        attaques=[
            griffe_ombre()
        ],

        passifs=[
            EROSION()
        ]
    )