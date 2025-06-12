from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.feuille_magique import feuille_magique
from data.attaques.nature.respiration import respiration
from data.attaques.nature.eolienne import eolienne

def soigneuse_astrale_des_bois():
    return Carte(

        nom="SOIGNEUSE ASTRALE DES BOIS",

        numero=71,

        rarete=TypeRarete.RARE,

        pv=500,

        element=Element.NATURE,

        attaques=[
            feuille_magique(),
            respiration(),
            eolienne()
        ],

        passifs=None
    )