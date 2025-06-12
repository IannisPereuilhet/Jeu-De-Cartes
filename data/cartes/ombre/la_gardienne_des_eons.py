from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.resurrection import resurrection
from data.attaques.ombre.aide_nocturne import aide_nocturne
from data.attaques.ombre.clair_de_lune import clair_de_lune

def la_gardienne_des_eons():
    return Carte(

        nom="LA GARDIENNE DES EONS",

        numero=95,

        rarete=TypeRarete.LEGENDAIRE,

        pv=550,

        element=Element.OMBRE,

        attaques=[
            resurrection(),
            aide_nocturne(),
            clair_de_lune()
        ],

        passifs=None
    )