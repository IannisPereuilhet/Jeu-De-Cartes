from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.molosse import molosse 
from data.attaques.nature.cuir_calcine import cuir_calcine

def leonid_cornubis():
    return Carte(

        nom="LEONID CORNUBIS",

        numero=182,

        rarete=TypeRarete.RARE,

        pv=500,

        element=Element.FEU,

        attaques=[
            molosse(),
            cuir_calcine()
        ],

        passifs=None,
    )