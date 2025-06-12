from utils import *
from src.attaque import Attaque
from src.effet import *

def odorat():
    return Attaque(
    
        nom="ODORAT",

        effets=[
            SOIN_ELEMENT(
                valeur=50,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=5,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.FEU
    )