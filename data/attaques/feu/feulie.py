from utils import *
from src.attaque import Attaque
from src.effet import *

def feulie():
    return Attaque(
    
        nom="FEULIE",

        effets=[
            BONUS_ELEMENT(
                valeur=10,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            )      
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.FEU: 5
                }
            ),

            USAGE_LIMITE(
                usage_limite=1
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.FEU
    )