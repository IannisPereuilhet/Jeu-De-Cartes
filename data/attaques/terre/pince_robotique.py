from utils import *
from src.attaque import Attaque
from src.effet import *

def pince_robotique():
    return Attaque(
    
        nom="PINCE ROBOTIQUE",

        effets=[
            DEGATS_ELEMENT(
                valeur=40,
                element=Element.ALEATOIRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
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