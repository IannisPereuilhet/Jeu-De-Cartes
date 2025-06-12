from utils import *
from src.attaque import Attaque
from src.effet import *

def phare():
    return Attaque(
    
        nom="PHARE",

        effets=[
            DEGATS_ELEMENT(
                valeur=45,
                element=Element.LUMIERE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=-0.2,
                cible=TypeCible.TOUS_LES_ENNEMIS
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.LUMIERE
    )