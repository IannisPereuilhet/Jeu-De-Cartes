from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.eclat_paisible import eclat_paisible
from data.attaques.lumiere.aide_pensive import aide_pensive

def dragonnet_des_lumieres():
    return Carte(

        nom="DRAGONNET DES LUMIERES",

        numero=42,

        rarete=TypeRarete.EPIQUE,

        pv=375,

        element=Element.LUMIERE,

        attaques=[
            eclat_paisible(),
            aide_pensive()
        ],

        passifs=None
    )