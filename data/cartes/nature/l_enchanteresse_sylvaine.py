from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.racines_maudites import racines_maudites

def l_enchanteresse_sylvaine():
    return Carte(

        nom="L'ENCHANTERESSE SYLVAINE",

        numero=121,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.NATURE,

        attaques=[
            racines_maudites()
        ],

        passifs=[
            POISON()
        ]
    )