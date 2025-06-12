from utils import *
from src.attaque import Attaque
from src.effet import *

def empal_soin():
    return Attaque(
    
        nom="EMPAL-SOIN",

        effets=[
            DEGATS_ELEMENT(
                valeur=25,
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

        proba_critique=0.50,

        critique=2,

        recharge=3,

        element=Element.TERRE
    )