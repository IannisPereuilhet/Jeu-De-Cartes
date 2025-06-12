from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.tranche_sol import tranche_sol
from data.attaques.terre.multiboost import multiboost

def guerrier_des_neiges():
    return Carte(

        nom="GUERRIER DES NEIGES",

        numero=59,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            tranche_sol(),
            multiboost()
        ],

        passifs=None
    )