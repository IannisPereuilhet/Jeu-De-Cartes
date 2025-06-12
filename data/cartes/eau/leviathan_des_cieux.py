from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.ecras_eau import ecras_eau
from data.attaques.eau.ultime_repos import ultime_repos
from data.attaques.eau.vague import vague

def leviathan_des_cieux():
    return Carte(

        nom="LEVIATHAN DES CIEUX",

        numero=44,

        rarete=TypeRarete.LEGENDAIRE,

        pv=650,

        element=Element.EAU,

        attaques=[
            ecras_eau(),
            ultime_repos(),
            vague()
        ],

        passifs=None
    )