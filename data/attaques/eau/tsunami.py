from utils import *
from src.attaque import Attaque
from src.effet import *

def tsunami():
    return Attaque(
    
        nom="TSUNAMI",

        effets=[
            DEGATS_ELEMENT(
                valeur=60,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            ZONE()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=3,

        recharge=4,

        element=Element.EAU
    )