from utils import *
from src.attaque import Attaque
from src.effet import *

def souffle_critique():
    return Attaque(
    
        nom="SOUFFLE CRITIQUE",

        effets=[
            DEGATS_ELEMENT(
                valeur=15,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_CRITIQUE(
                valeur=0.05,
                cible=TypeCible.SOI_MEME
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