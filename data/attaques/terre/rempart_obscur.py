from utils import *
from src.attaque import Attaque
from src.effet import *

def rempart_obscur():
    return Attaque(
        
        nom="REMPART OBSCUR",

        effets=[
            BONUS_ELEMENT(
                valeur=3,
                element=Element.TERRE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.OMBRE,
                cible=TypeCible.JOUEUR
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=2,

        element=Element.TERRE
    )