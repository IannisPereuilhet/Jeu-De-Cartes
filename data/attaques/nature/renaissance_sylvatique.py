from utils import *
from src.attaque import Attaque
from src.effet import *

def renaissance_sylvatique():
    return Attaque(
    
        nom="RENAISSANCE SYLVATIQUE",

        effets=[
            PROBA_PRECISION(
                valeur=0.05,
                cible=TypeCible.TOUS_LES_ALLIES
            ),

            PROBA_CRITIQUE(
                valeur=0.05,
                cible=TypeCible.TOUS_LES_ALLIES
            ),

            PROVOCATION(
                duree=1,
                cible=TypeCible.UNE_CARTE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.NATURE
    )