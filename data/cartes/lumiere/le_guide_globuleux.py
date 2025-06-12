from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.cascade_etheree import cascade_etheree
from data.attaques.lumiere.ecran import ecran
from data.attaques.eau.vague import vague

def le_guide_globuleux():
    return Carte(

        nom="LE GUIDE GLOBULEUX",

        numero=130,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.LUMIERE,

        attaques=[
            cascade_etheree(),
            ecran(),
            vague()
        ],

        passifs=None
    )