from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.eclair_purificateur import eclair_purificateur
from data.attaques.lumiere.soin_de_lumiere import soin_de_lumiere

def leo():
    return Carte(

        nom="LEO",

        numero=35,

        rarete=TypeRarete.RARE,

        pv=425,

        element=Element.LUMIERE,

        attaques=[
            eclair_purificateur(),
            soin_de_lumiere()
        ],

        passifs=None
    )