from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.ailes_braisees import ailes_braisees

def l_aviateur_infernal():
    return Carte(

        nom="L'AVIATEUR INFERNAL",

        numero=80,

        rarete=TypeRarete.EPIQUE,

        pv=500,

        element=Element.FEU,

        attaques=[
            ailes_braisees()
        ],

        passifs=None
    )