from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.souffle_d_eau import souffle_d_eau
from data.attaques.eau.vague import vague

def esprit_de_l_eau():
    return Carte(

        nom="ESPRIT DE L'EAU",

        numero=2,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.EAU,

        attaques=[
            souffle_d_eau(),
            vague()
        ],

        passifs=None
    )