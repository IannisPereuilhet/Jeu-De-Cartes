from utils import *
from src.attaque import Attaque
from src.effet import *

def boule_tenebreuse():
    return Attaque(
    
        nom="BOULE TENEBREUSE",

        effets=[
            DEGATS_ELEMENT(
                valeur=40,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.5,

        proba_critique=0.5,

        critique=2,

        recharge=2,

        element=Element.OMBRE
    )