from utils import *
from src.attaque import Attaque
from src.effet import *

def bond_miraculeux():
    return Attaque(
    
        nom="BOND-MIRACULEUX",

        effets=[
            SOIN_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=None,

        effets_passifs=[
            RECHARGE_PROBA(
                valeur=0.5
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )