from utils import *
from src.attaque import Attaque
from src.effet import *

def drain_vital():
    return Attaque(
    
        nom="DRAIN VITAL",

        effets=[
            VOL_ELEMENT(
                valeur=3,
                element=Element.ALEATOIRE,
                cible=TypeCible.ADVERSAIRE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )