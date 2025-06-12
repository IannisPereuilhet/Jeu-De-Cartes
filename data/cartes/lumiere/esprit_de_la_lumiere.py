from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.souffle_de_lumiere import souffle_de_lumiere
from data.attaques.lumiere.ecran import ecran

def esprit_de_la_lumiere():
    return Carte(

        nom="ESPRIT DE LA LUMIERE",

        numero=6,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            souffle_de_lumiere(),
            ecran()
        ],

        passifs=None
    )