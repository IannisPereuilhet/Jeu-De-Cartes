from utils import *
from src.attaque import Attaque
from src.effet import *

def vent_argente():
    return Attaque(
    
        nom="VENT ARGENTE",

        effets=[
            [       
                DEGATS_ELEMENT(
                    valeur=20,
                    element=Element.LUMIERE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                ),

                DEGATS_ELEMENT(
                    valeur=20,
                    element=Element.OMBRE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                )
            ],
                

            [
                BONUS_ELEMENT(
                    valeur=4,
                    element=Element.LUMIERE,
                    cible=TypeCible.JOUEUR
                ),

                BONUS_ELEMENT(
                    valeur=4,
                    element=Element.OMBRE,
                    cible=TypeCible.JOUEUR
                )
            ] 
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.LUMIERE
    )