from utils import *
from src.attaque import Attaque
from src.effet import *

def dechainement_spectral():
    return Attaque(
    
        nom="DECHAINEMENT SPECTRAL",

        effets=[
            DEGATS_ELEMENT(
                valeur=50,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=6,
                element=Element.OMBRE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=6,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=6,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.OMBRE
    )