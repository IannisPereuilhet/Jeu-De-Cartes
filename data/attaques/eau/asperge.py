from utils import *
from src.attaque import Attaque
from src.effet import *

def asperge():
    return Attaque(
    
        nom="ASPERGE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=-0.05,
                cible=TypeCible.UNE_CARTE_ENNEMIE
            ),
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=1,

        element=Element.EAU
    )