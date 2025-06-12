from utils import *
from src.attaque import Attaque
from src.effet import *

def tranche_ombre():
    return Attaque(
    
        nom="TRANCHE-OMBRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=3,

        recharge=4,

        element=Element.OMBRE
    )