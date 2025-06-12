from utils import *
from src.attaque import Attaque
from src.effet import *

def resurrection():
    return Attaque(
    
        nom="RESURRECTION",

        effets=[
            RESURRECTION(
                valeur=0.5,
                cible=TypeCible.JOUEUR
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=8,

        element=Element.OMBRE
    )