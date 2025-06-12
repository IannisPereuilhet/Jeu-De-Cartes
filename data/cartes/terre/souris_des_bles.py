from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.epidemie import epidemie

def souris_des_bles():
    return Carte(

        nom="SOURIS DES BLES",

        numero=140,

        rarete=TypeRarete.RARE,

        pv=350,

        element=Element.TERRE,

        attaques=[
            epidemie()
        ],

        passifs=[
            DISPARITION()
        ]
    )