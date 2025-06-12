from utils import *
from src.attaque import Attaque
from src.effet import *

def protection_marine():
    return Attaque(
    
        nom="PROTECTION MARINE",

        effets=[
            SOIN_ELEMENT(
                valeur=80,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            PROVOCATION(
                duree=1,
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.EAU
    )