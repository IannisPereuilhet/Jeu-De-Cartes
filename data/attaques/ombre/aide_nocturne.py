from utils import *
from src.attaque import Attaque
from src.effet import *

def aide_nocturne():
    return Attaque(
    
        nom="AIDE NOCTURNE",

        effets=[
            SOIN_ELEMENT(
                valeur=20,
                element=Element.OMBRE,
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

        recharge=4,

        element=Element.OMBRE
    )