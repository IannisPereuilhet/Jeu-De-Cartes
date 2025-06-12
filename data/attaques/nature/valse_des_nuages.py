from utils import *
from src.attaque import Attaque
from src.effet import *

def valse_des_nuages():
    return Attaque(
    
        nom="VALSE DES NUAGES",

        effets=[
            DEGATS_ELEMENT(
                valeur=90,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=[
            USAGE_LIMITE(
                usage_limite=1
            )
        ],

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=5,

        element=Element.NATURE
    )