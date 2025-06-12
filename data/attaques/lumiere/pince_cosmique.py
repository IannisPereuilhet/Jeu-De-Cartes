from utils import *
from src.attaque import Attaque
from src.effet import *

def pince_cosmique():
    return Attaque(
    
        nom="PINCE COSMIQUE",

        effets=[
            DEGATS_ELEMENT(
                valeur=80,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.LUMIERE: 8
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )