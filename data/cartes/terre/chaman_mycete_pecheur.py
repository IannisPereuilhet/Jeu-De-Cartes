from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.champi_heal import champi_heal

def chaman_mycete_pecheur():
    return Carte(

        nom="CHAMAN MYCETE PECHEUR",

        numero=161,

        rarete=TypeRarete.COMMUNE,

        pv=300,

        element=Element.TERRE,

        attaques=[
            champi_heal()
        ],

        passifs=[
            IMMUNITE()
        ]
    )