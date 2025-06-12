from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.sortilege import sortilege
from data.attaques.feu.flamme_aceree import flamme_aceree
from data.attaques.feu.braise_chaude import braise_chaude

def pyra_flamme_cachee():
    return Carte(

        nom="PYRA : FLAMME CACHEE",

        numero=79,

        rarete=TypeRarete.EPIQUE,

        pv=500,

        element=Element.FEU,

        attaques=[
            sortilege(),
            flamme_aceree(),
            braise_chaude()
        ],

        passifs=None
    )