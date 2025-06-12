from utils import *
from src.attaque import Attaque
from src.effet import *

def materia_defensive():
    return Attaque(
    
        nom="MATERIA DEFENSIVE",

        effets=[
            [
                BONUS_ELEMENT(
                    valeur=7,
                    element=Element.TERRE,
                    cible=TypeCible.JOUEUR
                )
            ],

            [
                BONUS_ELEMENT(
                    valeur=7,
                    element=Element.OMBRE,
                    cible=TypeCible.JOUEUR
                )
            ],

            [
                BONUS_ELEMENT(
                    valeur=7,
                    element=Element.EAU,
                    cible=TypeCible.JOUEUR
                )
            ]     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.FEU
    )