from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.incandescence import incandescence
from data.attaques.feu.silenfeu import silenfeu

def lisa_la_dragonniere():
    return Carte(

        nom="LISA, LA DRAGONNIERE",

        numero=91,

        rarete=TypeRarete.LEGENDAIRE,

        pv=400,

        element=Element.FEU,

        attaques=[
            incandescence(),
            silenfeu()
        ],

        passifs=None
    )