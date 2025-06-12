from utils import *
from src.attaque import Attaque
from src.effet import *

def riposte():
    return Attaque(
    
        nom="RIPOSTE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.PV_BAS
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.EAU
    )