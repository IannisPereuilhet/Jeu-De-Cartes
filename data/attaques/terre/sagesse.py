from utils import *
from src.attaque import Attaque
from src.effet import *

def sagesse():
    return Attaque(
        
        nom="SAGESSE",

        effets=[
            BONUS_ELEMENT(
                valeur=2,
                element=Element.TERRE,
                cible=TypeCible.JOUEUR
            ), 

            BONUS_ELEMENT(
                valeur=2,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )