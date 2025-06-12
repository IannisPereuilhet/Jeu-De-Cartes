from utils import *
from src.attaque import Attaque
from src.effet import *

def lumieres():
    return Attaque(
    
        nom="LUMIERES",

        effets=[
            [
                BONUS_ELEMENT(
                    valeur=5,
                    element=Element.LUMIERE,
                    cible=TypeCible.JOUEUR
                )
            ],

            [
                BONUS_ELEMENT(
                    valeur=5,
                    element=Element.OMBRE,
                    cible=TypeCible.JOUEUR
                )
            ]     
        ],

        effets_critiques=None,

        effets_passifs=[
            USAGE_LIMITE(
                usage_limite=1
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )