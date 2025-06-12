from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.pince_robotique import pince_robotique
from data.attaques.terre.miniboost import miniboost

def crabe_joyau_monde():
    return Carte(

        nom="CRABE JOYAU-MONDE",

        numero=162,

        rarete=TypeRarete.RARE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            pince_robotique(),
            miniboost()
        ],

        passifs=None
    )