from utils import *
from src.attaque import Attaque
from src.effet import *

def embrasement():
    return Attaque(
    
        nom="EMBRASEMENT",

        effets=[
            PROBA_CRITIQUE(
                valeur=0.05,
                cible=TypeCible.TOUS_LES_ALLIES
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.FEU
    )