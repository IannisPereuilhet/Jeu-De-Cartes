from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.braise_chaude import braise_chaude
from data.attaques.feu.chaleur_divine import chaleur_divine
from data.attaques.feu.embrasement import embrasement

def souverain_des_flammes():
    return Carte(

        nom="SOUVERAIN DES FLAMMES",

        numero=43,

        rarete=TypeRarete.LEGENDAIRE,

        pv=450,

        element=Element.FEU,

        attaques=[
            braise_chaude(),
            chaleur_divine(),
            embrasement()
        ],

        passifs=None
    )