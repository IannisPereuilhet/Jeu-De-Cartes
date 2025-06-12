from utils import *
from src.attaque import Attaque
from src.effet import *

def amitie():
    return Attaque(
        
        nom="AMITIE",

        effets=[
            BONUS_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.JOUEUR
            )   
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=10,

        element=Element.NATURE
    )