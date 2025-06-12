from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.fin_du_monde import fin_du_monde
from data.attaques.terre.forteresse import forteresse

def protecteur_des_ruines():
    return Carte(

        nom="PROTECTEUR DES RUINES",

        numero=94,

        rarete=TypeRarete.LEGENDAIRE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            fin_du_monde(),
            forteresse()
        ],

        passifs=[
            REVANCHE()
        ]
    )