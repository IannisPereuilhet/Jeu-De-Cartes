from utils import *
from src.attaque import Attaque
from src.effet import *

def regenair():
    return Attaque(
    
        nom="REGENAIR",

        effets=[
            SOIN_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE_ALLIEE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE_ALLIEE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE_ALLIEE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE_ALLIEE,
                calcul=TypeCalcul.CLASSIQUE
            ) 
        ],

        effets_critiques=None,

        effets_passifs=[
            ALEATOIRE()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )