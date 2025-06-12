from utils import *
from src.attaque import Attaque
from src.effet import *

def flamme_aceree():
    return Attaque(
    
        nom="FLAMME ACEREE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )      
        ],

        effets_critiques=[
            DISPARITION(
                cible=TypeCible.UNE_CARTE
            )
        ],

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.FEU
    )