from utils import *
from src.attaque import Attaque
from src.effet import *

def fulivert():
    return Attaque(
    
        nom="FULIVERT",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.75,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.EAU
    )