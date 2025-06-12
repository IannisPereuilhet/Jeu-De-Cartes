from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.corne_25 import corne_25
from data.attaques.terre.corne_75 import corne_75

def cornu_mythologique():
    return Carte(

        nom="CORNU MYTHOLOGIQUE",

        numero=139,

        rarete=TypeRarete.RARE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            corne_25(),
            corne_75()
        ],

        passifs=None
    )