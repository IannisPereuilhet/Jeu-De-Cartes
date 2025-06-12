from utils import *
from src.attaque import Attaque
from src.effet import *

def tissage():
    return Attaque(
    
        nom="TISSAGE",

        effets=[
            ETERNITE(
                valeur=1,
                cible=TypeCible.UNE_CARTE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            RECHARGE_PROBA(
                valeur=0.33
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.OMBRE
    )