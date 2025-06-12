from utils import *
from src.attaque import Attaque
from src.effet import *

def soin_de_lumiere():
    return Attaque(
    
        nom="SOIN DE LUMIERE",

        effets=[
            SOIN_ELEMENT(
                valeur=20,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.LUMIERE
    )