from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.bond_cybernetique import bond_cybernetique

def bondisseur_metallique():
    return Carte(

        nom="BONDISSEUR MECANIQUE",

        numero=126,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.TERRE,

        attaques=[
            bond_cybernetique()
        ],

        passifs=None
    )