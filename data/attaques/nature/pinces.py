from utils import *
from src.attaque import Attaque
from src.effet import *

def pinces():
    return Attaque(
    
        nom="PINCES",

        effets=[
            DEGATS_ELEMENT(
                valeur=5,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=6,

        recharge=1,

        element=Element.NATURE
    )