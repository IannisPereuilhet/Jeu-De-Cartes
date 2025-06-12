from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.queue_allongee import queue_allongee

def suricate_elance():
    return Carte(

        nom="SURICATE ELANCE",

        numero=105,

        rarete=TypeRarete.COMMUNE,

        pv=325,

        element=Element.NATURE,

        attaques=[
            queue_allongee()
        ],

        passifs=None
    )