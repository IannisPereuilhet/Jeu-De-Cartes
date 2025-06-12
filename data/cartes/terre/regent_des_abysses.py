from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.tremblement import tremblement
from data.attaques.terre.rempart_obscur import rempart_obscur
from data.attaques.terre.avalement import avalement

def regent_des_abysses():
    return Carte(

        nom="REGENT DES ABYSSES",

        numero=86,

        rarete=TypeRarete.EPIQUE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            tremblement(),
            rempart_obscur(),
            avalement()
        ],  

        passifs=None
    )