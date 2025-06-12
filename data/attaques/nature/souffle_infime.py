from utils import *
from src.attaque import Attaque
from src.effet import *

def souffle_infime():
    return Attaque(
    
        nom="SOUFFLE INFIME",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            VOL_ELEMENT(
                valeur=1,
                element=Element.NATURE,
                cible=TypeCible.ADVERSAIRE
            ) 
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )