from utils import *
from src.attaque import Attaque
from src.effet import *

def sortilege():
    return Attaque(
    
        nom="SORTILEGE",

        effets=[
            PURGE(
                cible=TypeCible.UNE_CARTE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=6,

        element=Element.FEU
    )