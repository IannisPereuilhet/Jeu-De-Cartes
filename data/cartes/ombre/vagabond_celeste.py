from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.souffle_d_ombre import souffle_d_ombre
from data.attaques.ombre.visee import visee

def vagabond_celeste():
    return Carte(

        nom="VAGABOND CELESTE",

        numero=20,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.OMBRE,

        attaques=[
            souffle_d_ombre(),
            visee()
        ],

        passifs=[
            POISON()
        ]
    )