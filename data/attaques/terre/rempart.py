from utils import *
from src.attaque import Attaque
from src.effet import *

def rempart():
    return Attaque(
        
        nom="REMPART",

        effets=[
            BONUS_ELEMENT(
                valeur=1,
                element=Element.TERRE,
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