from utils import *
from src.attaque import Attaque
from src.effet import *

def incaflamme():
    return Attaque(
    
        nom="INCAFLAMME",

        effets=[
            BONUS_ELEMENT(
                valeur=5,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.5,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.FEU
    )