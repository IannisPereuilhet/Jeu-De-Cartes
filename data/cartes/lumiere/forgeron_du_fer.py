from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.ralentissement import ralentissement
from data.attaques.lumiere.marteau_lumineux import marteau_lumineux

def forgeron_du_fer():
    return Carte(

        nom="FORGERON_DU_FER",

        numero=64,

        rarete=TypeRarete.COMMUNE,

        pv=475,

        element=Element.LUMIERE,

        attaques=[
            ralentissement(),
            marteau_lumineux()
        ],

        passifs=None
    )