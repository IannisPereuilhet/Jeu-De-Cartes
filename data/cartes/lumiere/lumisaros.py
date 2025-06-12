from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.materia_pointilleuse import materia_pointilleuse
from data.attaques.lumiere.materia_explosive import materia_explosive

def lumisaros():
    return Carte(

        nom="LUMISAROS",

        numero=167,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            materia_pointilleuse(),
            materia_explosive()
        ],

        passifs=None
    )