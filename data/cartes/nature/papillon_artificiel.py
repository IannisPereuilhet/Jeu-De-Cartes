from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.butinage import butinage

def papillon_artificiel():
    return Carte(

        nom="PAPILLON ARTIFICIEL",

        numero=157,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            butinage()
        ],

        passifs=None
    )