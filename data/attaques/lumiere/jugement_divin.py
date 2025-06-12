from utils import *
from src.attaque import Attaque
from src.effet import *

def jugement_divin():
    return Attaque(
    
        nom="JUGEMENT DIVIN",

        effets=[
            BONUS_RENIT(
                element=Element.MULTI,
                cible=TypeCible.ADVERSAIRE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=7,

        element=Element.LUMIERE
    )