from utils import *
from src.attaque import Attaque
from src.effet import *

def multiboost():
    return Attaque(
        
        nom="MULTIBOOST",

        effets=[
            BONUS_ELEMENT(
                valeur=3,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.EAU,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.TERRE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.OMBRE,
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

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.TERRE
    )