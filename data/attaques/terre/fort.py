from utils import *
from src.attaque import Attaque
from src.effet import *

def fort():
    return Attaque(
    
        nom="FORT",

        effets=[
            PROVOCATION(
                duree=2,
                cible=TypeCible.UNE_CARTE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=4,

        element=Element.TERRE
    )