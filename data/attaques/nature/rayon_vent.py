from utils import *
from src.attaque import Attaque
from src.effet import *

def rayon_vent():
    return Attaque(
    
        nom="RAYON-VENT",

        effets=[
            DEGATS_ELEMENT(
                valeur=15,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.85,

        proba_critique=0.15,

        critique=2,

        recharge=3,

        element=Element.NATURE
    )