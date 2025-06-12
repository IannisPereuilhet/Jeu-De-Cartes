from utils import *
from src.attaque import Attaque
from src.effet import *

def aventure():
    return Attaque(
    
        nom="AVENTURE",

        effets=[
            VALEUR_DE_BASE(
                valeur=1,
                cible=TypeCible.UNE_CARTE
            ),

            PROBA_PRECISION(
                valeur=0.03,
                cible=TypeCible.UNE_CARTE
            ),

            PROBA_CRITIQUE(
                valeur=0.03,
                cible=TypeCible.UNE_CARTE
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