from utils import *
from src.attaque import Attaque
from src.effet import *

def transperce_air():
    return Attaque(
    
        nom="TRANSPERCE AIR",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.MULTIPLICATEUR_ELEMENT
            )
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.NATURE: "TOUS"
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )