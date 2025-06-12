from utils import *
from src.attaque import Attaque
from src.effet import *

def epidemie():
    return Attaque(
    
        nom="EPIDEMIE",

        effets=[
            SOIN_ELEMENT(
                valeur=500,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.TERRE
    )