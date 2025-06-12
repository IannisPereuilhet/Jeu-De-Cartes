from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.ecou_lave import ecou_lave
from data.attaques.feu.feulie import feulie

def felin_eruptif():
    return Carte(

        nom="FELIN ERUPTIF",

        numero=134,

        rarete=TypeRarete.COMMUNE,

        pv=375,

        element=Element.FEU,

        attaques=[
            ecou_lave(),
            feulie()
        ],

        passifs=None
    )