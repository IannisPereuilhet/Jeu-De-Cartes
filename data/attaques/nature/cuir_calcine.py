from utils import *
from src.attaque import Attaque
from src.effet import *

def cuir_calcine():
    return Attaque(
    
        nom="CUIR CALCINE",

        effets=[
            PV_MAX(
                valeur=25,
                cible=TypeCible.SOI_MEME
            )   
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )