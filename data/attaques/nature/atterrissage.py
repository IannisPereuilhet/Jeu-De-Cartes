from utils import *
from src.attaque import Attaque
from src.effet import *

def atterrissage():
    return Attaque(
    
        nom="ATTERRISSAGE",

        effets=[
            SOIN_ELEMENT(
                valeur=30,
                element=Element.NATURE,
                cible=TypeCible.TOUS_LES_ALLIES,
                calcul=TypeCalcul.CLASSIQUE
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.NATURE
    )