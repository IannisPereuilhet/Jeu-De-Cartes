from utils import *
from src.attaque import Attaque
from src.effet import *

def tenebr_eal():
    return Attaque(
    
        nom="TENEBR'EAL",

        effets=[
            DEGATS_ELEMENT(
                valeur=40,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            VAMPIRISME()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.OMBRE
    )