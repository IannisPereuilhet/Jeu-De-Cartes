from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.pincement import pincement

def planeur_de_la_foret():
    return Carte(

        nom="PLANTEUR DE LA FORET",

        numero=62,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            pincement()
        ],

        passifs=[
            VENGEUR()
        ]
    )