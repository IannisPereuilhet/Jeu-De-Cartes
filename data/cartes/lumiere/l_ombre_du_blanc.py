from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.croc_blanc import croc_blanc
from data.attaques.nature.apaisement import apaisement

def l_ombre_du_blanc():
    return Carte(

        nom="L'OMBRE DU BLANC",

        numero=131,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            croc_blanc(),
            apaisement()
        ],

        passifs=None
    )