from utils import *
from src.attaque import Attaque
from src.effet import *

def amour():
    return Attaque(
        
        nom="AMOUR",

        effets=[
            PV_MAX(
                valeur=150,
                cible=TypeCible.UNE_CARTE
            )   
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=10,

        element=Element.NATURE
    )