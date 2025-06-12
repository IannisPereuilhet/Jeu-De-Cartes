from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.dechainement_spectral import dechainement_spectral
from data.attaques.ombre.obscur import obscur

def sombre_messager_des_nuages():
    return Carte(

        nom="SOMBRE MESSAGER DES NUAGES",

        numero=141,

        rarete=TypeRarete.RARE,

        pv=500,

        element=Element.OMBRE,

        attaques=[
            dechainement_spectral()
        ],

        passifs=[
            REVANCHE(),

            IMMUNITE()
        ]
    )