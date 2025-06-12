from utils import *
from src.attaque import Attaque
from src.effet import *

def etreinte_florale():
    return Attaque(
    
        nom="ETREINTE FLORALE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.EAU,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=30,
                element=Element.NATURE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            ),

            ETERNITE(
                valeur=1,
                cible=TypeCible.TOUS_LES_ENNEMIS
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            USAGE_LIMITE(
                usage_limite=2
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.EAU
    )