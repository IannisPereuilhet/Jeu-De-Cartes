from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.vague_de_sable import vague_de_sable
from data.attaques.terre.controle_de_terre import controle_de_terre
from data.attaques.terre.forteresse import forteresse

def le_gardien_des_dunes():
    return Carte(

        nom="LE GARDIEN DES DUNES",

        numero=46,

        rarete=TypeRarete.LEGENDAIRE,

        pv=425,

        element=Element.TERRE,

        attaques=[
            vague_de_sable(),
            controle_de_terre(),
            forteresse()
        ],

        passifs=None
    )