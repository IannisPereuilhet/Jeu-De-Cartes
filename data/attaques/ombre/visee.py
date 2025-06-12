from utils import *
from src.attaque import Attaque
from src.effet import *

def visee():
    return Attaque(
        
        nom="VISEE",

        effets=[
            ETERNITE(
                valeur=1,
                cible=TypeCible.UNE_CARTE),
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.7,

        proba_critique=0.05,

        critique=2,

        recharge=3,

        element=Element.OMBRE
    )