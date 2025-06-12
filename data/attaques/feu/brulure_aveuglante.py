from utils import *
from src.attaque import Attaque
from src.effet import *

def brulure_aveuglante():
    return Attaque(
    
        nom="BRULURE AVEUGLANTE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=-0.08,
                cible=TypeCible.UNE_CARTE_ENNEMIE
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.FEU
    )