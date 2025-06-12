from utils import *
from src.attaque import Attaque
from src.effet import *

def glace():
    return Attaque(
        
        nom="GLACE",

        effets=[
            DEGATS_ELEMENT(
                valeur=25,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=10
            ),

            COUT(
                cout={
                    Element.NATURE: 4
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.EAU
    )