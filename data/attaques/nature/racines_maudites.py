from utils import *
from src.attaque import Attaque
from src.effet import *

def racines_maudites():
    return Attaque(
    
        nom="RACINES MAUDITES",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.OMBRE,
                cible=TypeCible.JOUEUR
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.1,

        critique=2,

        recharge=3,

        element=Element.NATURE
    )