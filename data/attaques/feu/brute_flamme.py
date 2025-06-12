from utils import *
from src.attaque import Attaque
from src.effet import *

def brute_flamme():
    return Attaque(
    
        nom="BRUTE-FLAMME",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.TERRE,
                cible=TypeCible.JOUEUR
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.FEU
    )