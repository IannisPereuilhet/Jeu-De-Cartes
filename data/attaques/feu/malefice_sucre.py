from utils import *
from src.attaque import Attaque
from src.effet import *

def malefice_sucre():
    return Attaque(
        
        nom="MALEFICE SUCRE",

        effets=[
            SOIN_ELEMENT(
                valeur=5,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=5,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=5,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.OMBRE,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
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