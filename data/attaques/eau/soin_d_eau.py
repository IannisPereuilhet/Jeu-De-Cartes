from utils import *
from src.attaque import Attaque
from src.effet import *

def soin_d_eau():
    return Attaque(
    
        nom="SOIN D'EAU",

        effets=[
            SOIN_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.EAU
    )