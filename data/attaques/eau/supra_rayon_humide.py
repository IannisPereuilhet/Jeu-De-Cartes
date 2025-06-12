from utils import *
from src.attaque import Attaque
from src.effet import *

def supra_rayon_humide():
    return Attaque(
    
        nom="SUPRA-RAYON-HUMIDE",

        effets=[
            DEGATS_ELEMENT(
                valeur=25,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=25,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=25,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=5,
                element=Element.EAU,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=5,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=5,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.EAU
    )