from utils import *
from src.attaque import Attaque
from src.effet import *

def gobe_pierre():
    return Attaque(
    
        nom="GOBE-PIERRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=0,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )      
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=50
            ),

            COUT(
                cout={
                    Element.TERRE: 8
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=0,

        element=Element.TERRE
    )