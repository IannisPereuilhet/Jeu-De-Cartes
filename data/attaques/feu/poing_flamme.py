from utils import *
from src.attaque import Attaque
from src.effet import *

def poing_flamme():
    return Attaque(
    
        nom="POING-FLAMME",

        effets=[
            DEGATS_ELEMENT(
                valeur=50,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.FEU: 2,
                    Element.TERRE: 2
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.FEU
    )