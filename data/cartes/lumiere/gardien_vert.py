from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.rayonnement import rayonnement
from data.attaques.nature.respiration import respiration

def gardien_vert():
    return Carte(

        nom="GARDIEN VERT",

        numero=78,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            rayonnement(),
            respiration()
        ],

        passifs=None
    )