from utils import *
from src.attaque import Attaque
from src.effet import *

def aide_pensive():
    return Attaque(
        
        nom="AIDE PENSIVE",

        effets=[
            TEMPORALITE(
                valeur=1,
                cible=TypeCible.UNE_CARTE
            )   
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=3,

        element=Element.LUMIERE
    )