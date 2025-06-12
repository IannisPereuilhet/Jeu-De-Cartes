from utils import *
from src.attaque import Attaque
from src.effet import *

def appel_de_la_foret():
    return Attaque(
    
        nom="APPEL DE LA FORET",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.NATURE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.NATURE
    )