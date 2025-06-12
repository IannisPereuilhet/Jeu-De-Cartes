from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.lucky_fire import lucky_fire

def ignatius_le_dragon_flamme():
    return Carte(

        nom="IGNATIUS LE DRAGON FLAMME",

        numero=67,

        rarete=TypeRarete.RARE,

        pv=325,

        element=Element.FEU,

        attaques=[
            lucky_fire()
        ],

        passifs=None
    )