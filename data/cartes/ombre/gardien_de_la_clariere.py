from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.boule_tenebreuse import boule_tenebreuse

def gardien_de_la_clariere():
    return Carte(

        nom="GARDIEN DE LA CLARIERE",

        numero=19,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.OMBRE,

        attaques=[
            boule_tenebreuse(),
        ],

        passifs=[
            VENGEUR()
        ]
    )