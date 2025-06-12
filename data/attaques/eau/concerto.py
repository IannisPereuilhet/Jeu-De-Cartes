from utils import *
from src.attaque import Attaque
from src.effet import *

def concerto():
    return Attaque(
        
        nom="CONCERTO",

        effets=[
            BONUS_ELEMENT(
                valeur=50,
                element=Element.EAU,
                cible=TypeCible.JOUEUR
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=7,

        element=Element.EAU
    )