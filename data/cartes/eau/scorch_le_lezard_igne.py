from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.feau import feau

def scorch_le_lezard_igne():
    return Carte(

        nom="SCORCH, LE LEZARD IGNE",

        numero=69,

        rarete=TypeRarete.RARE,        

        pv=200,

        element=Element.EAU,

        attaques=[
            feau()
        ],

        passifs=[
            SOIN_PRIMITIF()
        ]
    )