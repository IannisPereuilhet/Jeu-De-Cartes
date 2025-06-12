from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.secousse_aleatoire import secousse_aleatoire
from data.attaques.nature.bond_chanceux import bond_chanceux

def aurora_majeste_feline():
    return Carte(

        nom="AURORA, MAJESTE FELINE",

        numero=31,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.TERRE,

        attaques=[
            secousse_aleatoire(),
            bond_chanceux()
        ],

        passifs=None
    )