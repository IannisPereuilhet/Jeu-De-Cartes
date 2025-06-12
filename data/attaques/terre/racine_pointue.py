from utils import *
from src.attaque import Attaque
from src.effet import *

def racine_pointue():
    return Attaque(
        
        nom="RACINE POINTUE",

        effets=[
            PV_MAX(
                valeur=-10,
                cible=TypeCible.TOUS_LES_ENNEMIS
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.TERRE
    )