from utils import *
from src.attaque import Attaque
from src.effet import *

def double_souffle():
    return Attaque(
    
        nom="DOUBLE SOUFFLE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=30,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=30,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.5,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.NATURE
    )