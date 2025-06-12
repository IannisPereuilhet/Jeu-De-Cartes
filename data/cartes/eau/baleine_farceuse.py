from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.hydrochance import hydrochance
from data.attaques.eau.ohohohohohoh import ohohohohohoh

def baleine_farceuse():
    return Carte(

        nom="BALEINE FARCEUSE",

        numero=82,

        rarete=TypeRarete.EPIQUE,

        pv=600,

        element=Element.EAU,

        attaques=[
            hydrochance(),
            ohohohohohoh()
        ],

        passifs=None
    )