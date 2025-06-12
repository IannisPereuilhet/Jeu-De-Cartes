from utils import *
from src.attaque import Attaque
from src.effet import *

def tornade():
    return Attaque(
    
        nom="TORNADE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=-0.02,
                cible=TypeCible.UNE_CARTE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.75,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )