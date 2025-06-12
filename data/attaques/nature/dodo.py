from utils import *
from src.attaque import Attaque
from src.effet import *

def dodo():
    return Attaque(
    
        nom="DODO",

        effets=[
            SOIN_ELEMENT(
                valeur=60,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            PROVOCATION(
                duree=1
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.NATURE
    )