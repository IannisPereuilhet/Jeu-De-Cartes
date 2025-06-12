from utils import *
from src.attaque import Attaque
from src.effet import *

def bulles():
    return Attaque(
    
        nom="BULLES",

        effets=[
            SOIN_ELEMENT(
                valeur=50,
                element=Element.EAU,
                cible=TypeCible.TOUS_LES_ALLIES,
                calcul=TypeCalcul.CLASSIQUE
            ) 
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.EAU
    )