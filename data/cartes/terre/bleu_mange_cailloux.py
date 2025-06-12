from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.gobe_pierre import gobe_pierre

def bleu_mange_cailloux():
    return Carte(

        nom="BLEU-MANGE-CAILLOUX",

        numero=85,

        rarete=TypeRarete.EPIQUE,

        pv=350,

        element=Element.TERRE,

        attaques=[
            gobe_pierre(),
        ],

        passifs=[
            REVANCHE()
        ]
    )