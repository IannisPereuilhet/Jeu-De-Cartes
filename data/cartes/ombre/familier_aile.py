from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.destin_aile import destin_aile

def familier_aile():
    return Carte(

        nom="FAMILIER AILE",

        numero=163,

        rarete=TypeRarete.COMMUNE,

        pv=300,

        element=Element.OMBRE,

        attaques=[
            destin_aile()
        ],

        passifs=None
    )