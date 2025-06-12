from utils import *
from src.attaque import Attaque
from src.effet import *

def chute_precise():
    return Attaque(
    
        nom="CHUTE PRECISE",

        effets=[
            PROBA_PRECISION(
                valeur=0.25,
                cible=TypeCible.UNE_CARTE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.01,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.OMBRE
    )