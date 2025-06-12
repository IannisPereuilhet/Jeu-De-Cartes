from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.duombre import duombre
from data.attaques.eau.aqua_sombre import aqua_sombre

def frost_de_la_toundra():
    return Carte(

        nom="FROST DE LA TOUNDRA",

        numero=34,

        rarete=TypeRarete.RARE,

        pv=425,

        element=Element.OMBRE,

        attaques=[
            duombre(),
            aqua_sombre()
        ],

        passifs=None
    )