from utils import *
from src.attaque import Attaque
from src.effet import *

def boost_chanceux():
    return Attaque(
    
        nom="BOOST CHANCEUX",

        effets=[
            BONUS_ELEMENT(
                valeur=1,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            )  
        ],

        effets_critiques=None,

        effets_passifs=[
            RECHARGE_PROBA(
                valeur=0.5
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )