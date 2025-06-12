from utils import *
from src.attaque import Attaque
from src.effet import *

def soin_tribu():
    return Attaque(
    
        nom="SOIN TRIBU",

        effets=[
            SOIN_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.TOUTES_LES_CARTES,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.FEU
    )