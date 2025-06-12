from utils import *
from src.attaque import Attaque
from src.effet import *

def etranglement():
    return Attaque(
    
        nom="ETRANGLEMENT",

        effets=[
            ETOURDISSEMENT(
                duree=2,
                cible=TypeCible.UNE_CARTE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.TERRE: 4
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.TERRE
    )