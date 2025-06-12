from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.brulure import brulure

def insecte_flammeveille():
    return Carte(

        nom="INSECTE FLAMMEVEILLE",

        numero=169,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.FEU,

        attaques=[
            brulure()
        ],

        passifs=[
            MYSTERE()
        ]
    )