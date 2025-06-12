from utils import *
from src.attaque import Attaque
from src.effet import *

def rayonnement():
    return Attaque(
    
        nom="RAYONNEMENT",

        effets=[
            DEGATS_ELEMENT(
                valeur=80,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            RECHARGE_MAX(
                cible=TypeCible.UNE_CARTE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.LUMIERE
    )