from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.protection_marine import protection_marine

def dame_navire():
    return Carte(

        nom="DAME NAVIRE",

        numero=101,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.EAU,

        attaques=[
            protection_marine()
        ],

        passifs=[
            TEMPORALITE()
        ]
    )