from utils import *
from src.attaque import Attaque
from src.effet import *

def incendie():
    return Attaque(
        
        nom="INCENDIE",

        effets=[
            DEGATS_ELEMENT(
                valeur=5,
                element=Element.FEU,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=1,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            ) 
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.5,

        critique=4,

        recharge=1,

        element=Element.FEU
    )