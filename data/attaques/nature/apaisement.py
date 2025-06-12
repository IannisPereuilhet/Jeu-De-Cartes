from utils import *
from src.attaque import Attaque
from src.effet import *

def apaisement():
    return Attaque(
        
        nom="APAISEMENT",

        effets=[
            SOIN_ELEMENT(
                valeur=5,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=5
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=4,

        recharge=1,

        element=Element.NATURE
    )