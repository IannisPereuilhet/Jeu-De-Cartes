from utils import *
from src.attaque import Attaque
from src.effet import *

def air_pur():
    return Attaque(
    
        nom="AIR PUR",

        effets=[
            DISPARITION(
                cible=TypeCible.UNE_CARTE
            ),

            PROBA_CRITIQUE(
                valeur=0.5,
                cible=TypeCible.UNE_CARTE
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.NATURE
    )