from utils import *
from src.attaque import Attaque
from src.effet import *

def soin_soleil():
    return Attaque(
    
        nom="SOIN SOLEIL",

        effets=[
            SOIN_ELEMENT(
                valeur=50,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            ETOURDISSEMENT()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.LUMIERE
    )