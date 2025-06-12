from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.torche import torche
from data.attaques.feu.temperature_ambiante import temperature_ambiante

def createur_de_la_fusion():
    return Carte(

        nom="CREATEUR DE LA FUSION",

        numero=68,

        rarete=TypeRarete.RARE,

        pv=500,

        element=Element.FEU,

        attaques=[
            torche(),
            temperature_ambiante()
        ],

        passifs=None
    )