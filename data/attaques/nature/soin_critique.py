from utils import *
from src.attaque import Attaque
from src.effet import *

def soin_critique():
    return Attaque(
    
        nom="SOIN CRITIQUE",

        effets=[
            SOIN_ELEMENT(
                valeur=20,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=[
            PROBA_CRITIQUE(
                valeur=0.1,
                cible=TypeCible.UNE_CARTE
            )
        ],

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.5,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )