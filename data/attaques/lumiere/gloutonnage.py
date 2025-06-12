from utils import *
from src.attaque import Attaque
from src.effet import *

def gloutonnage():
    return Attaque(
    
        nom="GLOUTONNAGE",

        effets=[
            PV_MAX(
                valeur=20,
                cible=TypeCible.SOI_MEME
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.LUMIERE: 1
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=0,

        element=Element.LUMIERE
    )