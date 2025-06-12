from utils import *
from src.attaque import Attaque
from src.effet import *

def feu_humide():
    return Attaque(
    
        nom="FEU HUMIDE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=4,   
                element=Element.EAU,
                cible=TypeCible.JOUEUR
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.FEU
    )