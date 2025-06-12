from utils import *
from src.attaque import Attaque
from src.effet import *

def laser_glacial():
    return Attaque(
    
        nom="LASER GLACIAL",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.1,

        proba_critique=0.01,

        critique=10,

        recharge=1,

        element=Element.EAU
    )