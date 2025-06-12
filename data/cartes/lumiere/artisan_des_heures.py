from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.ralentissement import ralentissement
from data.attaques.lumiere.flash import flash

def artisan_des_heures():
    return Carte(

        nom="ARTISAN DES HEURES",

        numero=23,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.LUMIERE,

        attaques=[
            ralentissement(),
            flash()
        ],

        passifs=None
    )