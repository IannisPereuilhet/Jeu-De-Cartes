from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.souffle_infime import souffle_infime

def elytre_etourdi():
    return Carte(

        nom="ELYTRE ETOURDI",

        numero=14,

        rarete=TypeRarete.COMMUNE,

        pv=300,

        element=Element.NATURE,

        attaques=[
            souffle_infime()
        ],

        passifs=[
            TERRAIN()
        ]
    )