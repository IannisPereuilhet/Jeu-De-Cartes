from utils import *
from src.attaque import Attaque
from src.effet import *

def fond_marin():
    return Attaque(
        
        nom="FOND MARIN",

        effets=[
            PROBA_PRECISION(
                valeur=0.12,
                cible=TypeCible.UNE_CARTE_ALLIEE
            ) 
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.EAU
    )