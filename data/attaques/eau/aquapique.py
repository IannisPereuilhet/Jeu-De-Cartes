from utils import *
from src.attaque import Attaque
from src.effet import *

def aquapique():
    return Attaque(
    
        nom="AQUAPIQUE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=4,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=4,
                element=Element.EAU,
                cible=TypeCible.JOUEUR
            ),

            PROVOCATION(
                duree=1,
                cible=TypeCible.UNE_CARTE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=4,

        element=Element.EAU
    )