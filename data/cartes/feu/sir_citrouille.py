from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.malefice_sucre import malefice_sucre

def sir_citrouille():
    return Carte(

        nom="SIR CITROUILLE",

        numero=181,

        rarete=TypeRarete.RARE,

        pv=300,

        element=Element.FEU,

        attaques=[
            malefice_sucre()
        ],

        passifs=[
            VENGEUR()
        ]
    )