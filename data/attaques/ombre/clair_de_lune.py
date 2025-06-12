from utils import *
from src.attaque import Attaque
from src.effet import *

def clair_de_lune():
    return Attaque(
    
        nom="CLAIR DE LUNE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.OMBRE
    )