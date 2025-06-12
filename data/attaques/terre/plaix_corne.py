from utils import *
from src.attaque import Attaque
from src.effet import *

def plaix_corne():
    return Attaque(
    
        nom="PLAIX-CORNE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=1,
                element=Element.TERRE,
                cible=TypeCible.JOUEUR
            ),

            PROBA_CRITIQUE(
                valeur=0.05,
                cible=TypeCible.SOI_MEME
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=3,

        recharge=1,

        element=Element.TERRE
    )