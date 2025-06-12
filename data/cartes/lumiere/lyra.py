from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.electro_choc import electro_choc
from data.attaques.lumiere.magie_de_lyra import magie_de_lyra

def lyra():
    return Carte(

        nom="LYRA",

        numero=144,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            electro_choc(),
            magie_de_lyra()
        ],

        passifs=None
    )