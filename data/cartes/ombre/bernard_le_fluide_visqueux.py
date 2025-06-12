from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.bain_de_boue import bain_de_boue

def bernard_le_fluide_visqueux():
    return Carte(

        nom="BERNARD, LE FLUIDE VISQUEUX",

        numero=164,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.OMBRE,

        attaques=[
            bain_de_boue()
        ],

        passifs=[
            RESET()
        ]
    )