from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.malediction_aquatique import malediction_aquatique
from data.attaques.eau.vague import vague
from data.attaques.nature.eolienne import eolienne

def zombie_floral():
    return Carte(

        nom="ZOMBIE FLORAL",

        numero=174,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.NATURE,

        attaques=[
            malediction_aquatique(),
            vague(),
            eolienne()
        ],

        passifs=None
    )