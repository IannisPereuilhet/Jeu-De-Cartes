from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.visee_offensive import visee_offensive
from data.attaques.nature.bond_chanceux import bond_chanceux

def felin_errant():
    return Carte(

        nom="FELIN ERRANT",

        numero=21,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            visee_offensive(),
            bond_chanceux()
        ],

        passifs=None
    )