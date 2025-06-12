from utils import *
from src.attaque import Attaque
from src.effet import *

def regurgitation():
    return Attaque(
    
        nom="REGURGITATION",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.PV_MAX
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.LUMIERE
    )