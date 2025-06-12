from utils import *
from src.attaque import Attaque
from src.effet import *

def torche():
    return Attaque(
    
        nom="TORCHE",

        effets=[
            DISPARITION(
                cible=TypeCible.UNE_CARTE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=6,

        element=Element.FEU
    )