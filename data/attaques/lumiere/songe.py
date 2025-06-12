from utils import *
from src.attaque import Attaque
from src.effet import *

def songe():
    return Attaque(
    
        nom="SONGE",

        effets=[
            [
                BONUS_ELEMENT(
                    valeur=9,
                    element=Element.LUMIERE,
                    cible=TypeCible.JOUEUR
                ),

                BONUS_ELEMENT(
                    valeur=9,
                    element=Element.NATURE,
                    cible=TypeCible.JOUEUR
                )
            ],

            [
                PURGE(
                    cible=TypeCible.UNE_CARTE
                )
            ]                  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=6,

        element=Element.LUMIERE
    )