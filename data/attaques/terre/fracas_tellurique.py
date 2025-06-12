from utils import *
from src.attaque import Attaque
from src.effet import *

def fracas_tellurique():
    return Attaque(
    
        nom="FRACAS TELLURIQUE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            CONTRECOUP()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )