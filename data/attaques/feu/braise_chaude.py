from utils import *
from src.attaque import Attaque
from src.effet import *

def braise_chaude():
    return Attaque(
    
        nom="BRAISE CHAUDE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_CRITIQUE(
                valeur=0.02,
                cible=TypeCible.TOUS_LES_ALLIES
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.FEU
    )