from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.grain_de_sable import grain_de_sable

def le_sableux_sifflant():
    return Carte(

        nom="LE SABLEUX SIFFLANT",

        numero=18,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.TERRE,

        attaques=[
            grain_de_sable(),
        ],

        passifs=None
    )