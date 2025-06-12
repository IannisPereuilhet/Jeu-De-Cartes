from utils import *
from src.attaque import Attaque
from src.effet import *

def embrasement_critique():
    return Attaque(
    
        nom="EMBRASEMENT CRITIQUE",

        effets=[
            PROBA_CRITIQUE(
                valeur=0.5,
                cible=TypeCible.TOUTES_LES_CARTES
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=5,

        element=Element.FEU
    )