from utils import *
from src.attaque import Attaque
from src.effet import *

def vent_critique():
    return Attaque(
    
        nom="VENT CRITIQUE",

        effets=[
            SOIN_ELEMENT(
                valeur=40,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=None,

        effets_passifs=[
            ETOURDISSEMENT(
                duree=1
            )
        ],

        proba_precision=1.0,

        proba_critique=0.2,

        critique=2,

        recharge=4,

        element=Element.NATURE
    )