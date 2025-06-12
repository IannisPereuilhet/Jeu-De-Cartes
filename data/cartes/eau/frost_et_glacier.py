from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.eau_trouble import eau_trouble

def frost_et_glacier():
    return Carte(

        nom="FROST ET GLACIER",

        numero=92,

        rarete=TypeRarete.LEGENDAIRE,

        pv=400,

        element=Element.EAU,

        attaques=[
            eau_trouble()
        ],

        passifs=[
            ETOURDISSEMENT(),
            EROSION()
        ]
    )