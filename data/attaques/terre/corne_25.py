from utils import *
from src.attaque import Attaque
from src.effet import *

def corne_25():
    return Attaque(
    
        nom="CORNE 25",

        effets=[
            PV_POURCENTAGE(
                valeur=0.25,
                cible=TypeCible.UNE_CARTE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.TERRE
    )