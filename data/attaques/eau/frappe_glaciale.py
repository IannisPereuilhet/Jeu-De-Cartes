from utils import *
from src.attaque import Attaque
from src.effet import *

def frappe_glaciale():
    return Attaque(
    
        nom="FRAPPE GLACIALE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=30,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=30,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=30,
                element=Element.EAU,
                cible=TypeCible.SOI_MEME,
                calcul=TypeCalcul.CLASSIQUE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.5,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.EAU
    )