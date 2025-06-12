from utils import *
from src.attaque import Attaque
from src.effet import *

def cascade_etheree():
    return Attaque(
    
        nom="CASCADE ETHEREE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            EROSION()
        ],

        proba_precision=1.0,

        proba_critique=0.15,

        critique=2,

        recharge=3,

        element=Element.LUMIERE
    )