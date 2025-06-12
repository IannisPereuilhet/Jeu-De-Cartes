from utils import *
from src.attaque import Attaque
from src.effet import *

def molosse():
    return Attaque(
    
        nom="MOLOSSE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            VAMPIRISME()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=4,

        recharge=1,

        element=Element.FEU
    )