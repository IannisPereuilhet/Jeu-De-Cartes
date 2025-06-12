from utils import *
from src.attaque import Attaque
from src.effet import *

def croc_terre():
    return Attaque(
    
        nom="CROC TERRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.7,

        proba_critique=0.01,

        critique=3,

        recharge=3,

        element=Element.TERRE
    )