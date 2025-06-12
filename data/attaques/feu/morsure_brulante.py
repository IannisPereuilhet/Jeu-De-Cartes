from utils import *
from src.attaque import Attaque
from src.effet import *

def morsure_brulante():
    return Attaque(
    
        nom="MORSURE BRULANTE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_CRITIQUE(
                valeur=0.1,
                cible=TypeCible.SOI_MEME
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.25,

        critique=2,

        recharge=3,

        element=Element.FEU
    )