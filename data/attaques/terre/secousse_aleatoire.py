from utils import *
from src.attaque import Attaque
from src.effet import *

def secousse_aleatoire():
    return Attaque(
    
        nom="SECOUSSE ALEATOIRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=80,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_CRITIQUE(
                valeur=0.25,
                cible=TypeCible.TOUS_LES_ALLIES
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.1,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )