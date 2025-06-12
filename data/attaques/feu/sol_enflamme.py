from utils import *
from src.attaque import Attaque
from src.effet import *

def sol_enflamme():
    return Attaque(
    
        nom="SOL ENFLAMME",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )      
        ],

        effets_critiques=[
            BONUS_ELEMENT(
                valeur=4,
                element=Element.TERRE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=4,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            )
        ],

        effets_passifs=None,

        proba_precision=0.75,

        proba_critique=0.25,

        critique=2,

        recharge=1,

        element=Element.FEU
    )