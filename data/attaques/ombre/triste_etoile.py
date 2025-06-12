from utils import *
from src.attaque import Attaque
from src.effet import *

def triste_etoile():
    return Attaque(
    
        nom="TRISTE ETOILE",

        effets=[
            DEGATS_ELEMENT(
                valeur=5,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=2
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.OMBRE
    )