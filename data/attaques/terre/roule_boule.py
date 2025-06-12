from utils import *
from src.attaque import Attaque
from src.effet import *

def roule_boule():
    return Attaque(
    
        nom="ROULE-BOULE",

        effets=[
            DEGATS_ELEMENT(
                valeur=15,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=5
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )