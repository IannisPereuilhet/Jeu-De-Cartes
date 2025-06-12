from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.gloutonnage import gloutonnage
from data.attaques.lumiere.regurgitation import regurgitation

def glouton_de_lueur():
    return Carte(

        nom="GLOUTON DE LUEUR",

        numero=112,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            gloutonnage(),
            regurgitation()
        ],

        passifs=None
    )