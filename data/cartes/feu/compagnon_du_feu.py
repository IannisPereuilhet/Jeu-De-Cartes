from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.odorat import odorat
from data.attaques.feu.brulure_aveuglante import brulure_aveuglante

def compagnon_du_feu():
    return Carte(

        nom="COMPAGNON DU FEU",

        numero=8,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.FEU,

        attaques=[
            odorat(),
            brulure_aveuglante()
        ],

        passifs=[
            FUMEE()
        ]
    )