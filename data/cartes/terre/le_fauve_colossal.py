from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.devalement import devalement
from data.attaques.nature.bond_rapide import bond_rapide
from data.attaques.nature.bond_chanceux import bond_chanceux

def le_fauve_colossal():
    return Carte(

        nom="LE FAUVE COLOSSAL",

        numero=73,

        rarete=TypeRarete.RARE,

        pv=300,

        element=Element.TERRE,

        attaques=[
            devalement(),
            bond_rapide(),
            bond_chanceux()
        ],

        passifs=None
    )