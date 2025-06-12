from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.glace import glace
from data.attaques.nature.eolienne import eolienne

def plumelotus_aquatique():
    return Carte(

        nom="PLUMELOTUS AQUATIQUE",

        numero=156,

        rarete=TypeRarete.COMMUNE,        

        pv=500,

        element=Element.EAU,

        attaques=[
            glace(),
            eolienne()
        ],

        passifs=None
    )