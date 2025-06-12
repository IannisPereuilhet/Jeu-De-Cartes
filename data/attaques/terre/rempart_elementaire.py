from utils import *
from src.attaque import Attaque
from src.effet import *

def rempart_elementaire():
    return Attaque(
        
        nom="REMPART ELEMENTAIRE",

        effets=[
            BONUS_ELEMENT(
                valeur=-1,
                element=Element.MULTI,
                cible=TypeCible.ADVERSAIRE
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.5,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )