from utils import *
from src.attaque import Attaque
from src.effet import *

def missile_terre_eau():
    return Attaque(
    
        nom="MISSILE TERRE-EAU",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=30,
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

        recharge=3,

        element=Element.EAU
    )