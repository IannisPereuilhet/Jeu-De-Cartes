from utils import *
from src.attaque import Attaque
from src.effet import *

def souffle_lent():
    return Attaque(
    
        nom="SOUFFLE LENT",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
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