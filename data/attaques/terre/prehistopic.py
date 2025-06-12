from utils import *
from src.attaque import Attaque
from src.effet import *

def prehistopic():
    return Attaque(
    
        nom="PREHISTOPIC",

        effets=[
            PV_MAX(
                valeur=100,
                cible=TypeCible.UNE_CARTE
            ),

            RECHARGE_MAX(
                cible=TypeCible.UNE_CARTE
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.TERRE
    )