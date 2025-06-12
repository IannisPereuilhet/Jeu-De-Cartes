from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.duombre import duombre
from data.attaques.nature.regenair import regenair

def complices_de_la_foret():
    return Carte(

        nom="COMPLICES DE LA FORET",

        numero=177,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.OMBRE,

        attaques=[
            duombre(),
            regenair()
        ],

        passifs=None
    )