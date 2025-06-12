from utils import *
from src.attaque import Attaque
from src.effet import *

def vitalite_chanceuse():
    return Attaque(
    
        nom="VITALITE CHANCEUSE",

        effets=[
            PV_MAX(
                valeur=5,
                cible=TypeCible.UNE_CARTE
            )  
        ],

        effets_critiques=None,

        effets_passifs=[
            RECHARGE_PROBA(
                valeur=0.5
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )