from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.aventure import aventure
from data.attaques.terre.rempart import rempart
from data.attaques.ombre.obscur import obscur

def gnome_aventurier():
    return Carte(

        nom="GNOME AVENTURIER",

        numero=176,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            aventure(),
            rempart(),
            obscur()
        ],

        passifs=None
    )