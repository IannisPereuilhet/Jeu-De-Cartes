from utils import *
from src.attaque import Attaque
from src.effet import *

def champi_heal():
    return Attaque(
    
        nom="CHAMPI'HEAL",

        effets=[
            SOIN_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=20,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=20,
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

        recharge=2,

        element=Element.TERRE
    )