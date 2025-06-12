from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.pansage import pansage
from data.attaques.nature.respiration import respiration

def le_lezard_lueur():
    return Carte(

        nom="LE LEZARD LUEUR",

        numero=24,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            pansage(),
            respiration()
        ],

        passifs=None
    )