from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.encre_seche import encre_seche

def poulpe_parleur():
    return Carte(

        nom="POULPE PARLEUR",

        numero=146,

        rarete=TypeRarete.EPIQUE,        

        pv=325,

        element=Element.EAU,

        attaques=[
            encre_seche()
        ],

        passifs=[
            FUMEE()
        ]
    )