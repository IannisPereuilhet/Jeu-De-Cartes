from utils import *
from src.attaque import Attaque
from src.effet import *

def nageoire_sifflante():
    return Attaque(
    
        nom="NAGEOIRE SIFFLANTE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=[
            BONUS_ELEMENT(
                valeur=2,
                element=Element.EAU,
                cible=TypeCible.JOUEUR
            ),

            BONUS_ELEMENT(
                valeur=2,
                element=Element.NATURE,
                cible=TypeCible.JOUEUR
            )
        ],

        effets_passifs=None,

        proba_precision=0.5,

        proba_critique=0.5,

        critique=2,

        recharge=1,

        element=Element.EAU
    )