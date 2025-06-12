from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.chaos_elementaire import chaos_elementaire
from data.attaques.terre.multiboost import multiboost

def maitre_des_teintes():
    return Carte(

        nom="MAITRE DES TEINTES",

        numero=32,

        rarete=TypeRarete.RARE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            chaos_elementaire(),
            multiboost()
        ],

        passifs=None
    )