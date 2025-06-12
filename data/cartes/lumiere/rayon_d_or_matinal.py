from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.eblouissement import eblouissement

def rayon_d_or_matinal():
    return Carte(

        nom="RAYON D'OR MATINAL",

        numero=65,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            eblouissement()
        ],

        passifs=[
            CIMETIERE()
        ]
    )