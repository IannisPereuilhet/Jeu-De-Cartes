from utils import *
from src.attaque import Attaque
from src.effet import *

def feu_allie():
    return Attaque(
    
        nom="FEU ALLIE",

        effets=[
            VALEUR_DE_BASE(
                valeur=4,
                cible=TypeCible.UNE_CARTE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.FEU
    )