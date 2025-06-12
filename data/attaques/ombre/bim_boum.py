from utils import *
from src.attaque import Attaque
from src.effet import *

def bim_boum():
    return Attaque(
        
        nom="BIM-BOUM",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.OMBRE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.LUMIERE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
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

        proba_precision=0.5,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.OMBRE
    )