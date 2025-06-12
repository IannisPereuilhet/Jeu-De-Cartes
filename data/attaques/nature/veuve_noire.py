from utils import *
from src.attaque import Attaque
from src.effet import *

def veuve_noire():
    return Attaque(
    
        nom="VEUVE NOIRE",

        effets=[
            SACRIFICE(
                cible=TypeCible.UNE_CARTE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=7,

        element=Element.NATURE
    )