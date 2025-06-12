from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.bond_chanceux import bond_chanceux
from data.attaques.nature.boost_chanceux import boost_chanceux
from data.attaques.nature.vitalite_chanceuse import vitalite_chanceuse

def fanure():
    return Carte(

        nom="FANURE",

        numero=84,

        rarete=TypeRarete.EPIQUE,

        pv=300,

        element=Element.NATURE,

        attaques=[
            bond_chanceux(),
            boost_chanceux(),
            vitalite_chanceuse()
        ],

        passifs=None
    )