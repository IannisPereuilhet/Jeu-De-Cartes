from utils import *
from src.attaque import Attaque
from src.effet import *

def sucre_doux():
    return Attaque(
    
        nom="SUCRE DOUX",

        effets=[
            [
                PURGE(
                    cible=TypeCible.UNE_CARTE
                )
            ],

            [
                DISPARITION(
                    cible=TypeCible.UNE_CARTE
                )
            ]     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.LUMIERE
    )