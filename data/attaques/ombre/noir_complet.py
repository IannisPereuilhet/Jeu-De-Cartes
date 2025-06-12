from utils import *
from src.attaque import Attaque
from src.effet import *

def noir_complet():
    return Attaque(
    
        nom="NOIR COMPLET",

        effets=[
            PROBA_PRECISION(
                valeur=-0.2,
                cible=TypeCible.UNE_CARTE_ENNEMIE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.OMBRE
    )