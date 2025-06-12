from utils import *
from src.attaque import Attaque
from src.effet import *

def tranche_sol():
    return Attaque(
    
        nom="TRANCHE-SOL",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=[
            BONUS_ELEMENT(
                valeur=1,
                element=Element.MULTI,
                cible=TypeCible.JOUEUR
            )
        ],

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.25,

        critique=4,

        recharge=2,

        element=Element.TERRE
    )