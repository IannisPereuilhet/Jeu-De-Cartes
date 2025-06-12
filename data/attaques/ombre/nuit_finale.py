from utils import *
from src.attaque import Attaque
from src.effet import *

def nuit_finale():
    return Attaque(
    
        nom="NUIT FINALE",

        effets=[
            RECHARGE_RENIT(
                cible=TypeCible.TOUS_LES_ALLIES
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=8,

        element=Element.OMBRE
    )