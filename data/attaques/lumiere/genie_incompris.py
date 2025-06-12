from utils import *
from src.attaque import Attaque
from src.effet import *

def genie_incompris():
    return Attaque(
        
        nom="GENIE INCOMPRIS",

        effets=[
            BONUS_ELEMENT(
                valeur=35,
                element=Element.ALEATOIRE,
                cible=TypeCible.JOUEUR
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