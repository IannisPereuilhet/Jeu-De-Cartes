from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.bim_boum import bim_boum

def spectre_canin():
    return Carte(

        nom="SPECTRE CANIN",

        numero=127,

        rarete=TypeRarete.COMMUNE,

        pv=550,

        element=Element.OMBRE,

        attaques=[
            bim_boum()
        ],

        passifs=[
            IMMUNITE()
        ]
    )