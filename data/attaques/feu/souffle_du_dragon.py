from utils import *
from src.attaque import Attaque
from src.effet import *

def souffle_du_dragon():
    return Attaque(
    
        nom="SOUFFLE DU DRAGON",

        effets=[
            [
                DEGATS_ELEMENT(
                    valeur=25,
                    element=Element.FEU,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                )
            ],

            [
                BONUS_ELEMENT(
                    valeur=5,
                    element=Element.FEU,
                    cible=TypeCible.JOUEUR
                ),

                BONUS_ELEMENT(
                    valeur=5,
                    element=Element.NATURE,
                    cible=TypeCible.JOUEUR
                )
            ]                  
        ],

        effets_critiques=None,

        effets_passifs=[
            ETOURDISSEMENT()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.FEU
    )