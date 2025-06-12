from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.asperge import asperge
from data.attaques.lumiere.voile_du_doute import voile_du_doute

def crapaud_de_cristal():
    return Carte(

        nom="CRAPAUD DE CRISTAL",

        numero=11,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.EAU,

        attaques=[
            asperge(),
            voile_du_doute()
        ],

        passifs=None
    )