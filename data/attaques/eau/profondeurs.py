from utils import *
from src.attaque import Attaque
from src.effet import *

def profondeurs():
    return Attaque(
        
        nom="PROFONDEURS",

        effets=[
            BONUS_ELEMENT(
                valeur=1,
                element=Element.EAU,
                cible=TypeCible.JOUEUR
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.OMBRE: 1
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=0,

        element=Element.EAU
    )