from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.pince_cosmique import pince_cosmique

def crustace_de_l_astre():
    return Carte(

        nom="CRUSTACE DE L'ASTRE",

        numero=166,

        rarete=TypeRarete.COMMUNE,

        pv=350,

        element=Element.LUMIERE,

        attaques=[
            pince_cosmique()
        ],

        passifs=None
    )