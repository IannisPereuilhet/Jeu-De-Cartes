from utils import *
from src.attaque import Attaque
from src.effet import *

def duombre():
    return Attaque(
    
        nom="DUOMBRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.OMBRE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=1,
                element=Element.OMBRE,
                cible=TypeCible.JOUEUR
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.OMBRE
    )