from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.songe import songe
from data.attaques.lumiere.boule_graine import boule_graine

def lumiflore_la_boule_de_lumiere():
    return Carte(

        nom="LUMIFLORE, LA BOULE DE LUMIERE",

        numero=132,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            songe(),
            boule_graine()
        ],

        passifs=None
    )