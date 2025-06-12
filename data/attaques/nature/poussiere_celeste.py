from utils import *
from src.attaque import Attaque
from src.effet import *

def poussiere_celeste():
    return Attaque(
    
        nom="POUSSIERE CELESTE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=-0.08,
                cible=TypeCible.TOUTES_LES_CARTES
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.NATURE
    )