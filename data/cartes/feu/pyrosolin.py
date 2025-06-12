from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.materia_offensive import materia_offensive
from data.attaques.feu.materia_defensive import materia_defensive

def pyrosolin():
    return Carte(

        nom="PYROSOLIN",

        numero=153,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.FEU,

        attaques=[
            materia_offensive(),
            materia_defensive()
        ],

        passifs=None
    )