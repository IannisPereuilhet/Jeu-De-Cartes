from utils import *
from src.attaque import Attaque
from src.effet import *

def souffle_eblouissant():
    return Attaque(
    
        nom="SOUFFLE EBLOUISSANT",

        effets=[
            DEGATS_ELEMENT(
                valeur=40,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.LUMIERE
    )