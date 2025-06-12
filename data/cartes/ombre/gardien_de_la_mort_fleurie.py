from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.triste_etoile import triste_etoile
from data.attaques.ombre.alliance_noire import alliance_noire

def gardien_de_la_mort_fleurie():
    return Carte(

        nom="GARDIEN DE LA MORT FLEURIE",

        numero=41,

        rarete=TypeRarete.EPIQUE,

        pv=550,

        element=Element.OMBRE,

        attaques=[
            triste_etoile(),
            alliance_noire()
        ],

        passifs=[
            CIMETIERE()
        ]
    )