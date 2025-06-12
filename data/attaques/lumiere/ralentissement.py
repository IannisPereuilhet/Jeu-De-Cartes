from utils import *
from src.attaque import Attaque
from src.effet import *

def ralentissement():
    return Attaque(
    
        nom="RALENTISSEMENT",

        effets=[
            ETERNITE(
                valeur=1,
                cible=TypeCible.UNE_CARTE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.LUMIERE
    )