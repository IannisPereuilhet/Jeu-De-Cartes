from utils import *
from src.attaque import Attaque
from src.effet import *

def aspireau():
    return Attaque(
    
        nom="ASPIREAU",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),
            
            VOL_ELEMENT(
                valeur=1,
                element=Element.EAU,
                cible=TypeCible.ADVERSAIRE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=10,

        recharge=2,

        element=Element.EAU
    )