from utils import *
from src.attaque import Attaque
from src.effet import *

def chanceur():
    return Attaque(
        
        nom="CHANCEUR",

        effets=[
            BONUS_ELEMENT(
                valeur=10,
                element=Element.ALEATOIRE,
                cible=TypeCible.JOUEUR
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=1,

        element=Element.FEU
    )