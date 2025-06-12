from utils import *
from src.attaque import Attaque
from src.effet import *

def ohohohohohoh():
    return Attaque(
    
        nom="OHOHOHOHOHOH",

        effets=[
            PROBA_CRITIQUE(
                valeur=0.5,
                cible=TypeCible.SOI_MEME
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=6,

        element=Element.EAU
    )