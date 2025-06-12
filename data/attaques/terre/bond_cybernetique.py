from utils import *
from src.attaque import Attaque
from src.effet import *

def bond_cybernetique():
    return Attaque(
    
        nom="BOND-CYBERNETIQUE",

        effets=[
            DEGATS_ELEMENT(
                valeur=[-25, 40],
                element=Element.TERRE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
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

        element=Element.TERRE
    )