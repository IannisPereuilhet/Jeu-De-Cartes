from utils import *
from src.attaque import Attaque
from src.effet import *

def lumiere_critique():
    return Attaque(
    
        nom="LUMIERE CRITIQUE",

        effets=[
            PROBA_CRITIQUE(
                valeur=0.05,
                cible=TypeCible.UNE_CARTE_ALLIEE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )