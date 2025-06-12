from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.bond_chanceux import bond_chanceux
from data.attaques.nature.bond_miraculeux import bond_miraculeux

def enfant_eucalyptus():
    return Carte(

        nom="ENFNANT EUCALYPTUS",

        numero=173,

        rarete=TypeRarete.COMMUNE,

        pv=300,

        element=Element.NATURE,

        attaques=[
            bond_chanceux(),
            bond_miraculeux()
        ],

        passifs=[
            EROSION()
        ]
    )