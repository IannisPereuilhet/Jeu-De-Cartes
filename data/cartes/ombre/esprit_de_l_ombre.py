from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.souffle_d_ombre import souffle_d_ombre
from data.attaques.ombre.obscur import obscur

def esprit_de_l_ombre():
    return Carte(

        nom="ESPRIT DE L'OMBRE",

        numero=5,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            souffle_d_ombre(),
            obscur()
        ],

        passifs=None
    )