from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.bruit_sombre import bruit_sombre
from data.attaques.ombre.noir_complet import noir_complet

def seigneur_paisible():
    return Carte(

        nom="SEIGNEUR PAISIBLE",

        numero=165,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            bruit_sombre(),
            noir_complet()
        ],

        passifs=[
            FUMEE()
        ]
    )