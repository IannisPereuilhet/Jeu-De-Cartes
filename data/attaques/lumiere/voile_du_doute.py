from utils import *
from src.attaque import Attaque
from src.effet import *

def voile_du_doute():
    return Attaque(
    
        nom="VOILE DU DOUTE",

        effets=[
            PROBA_PRECISION(
                valeur=-0.05,
                cible=TypeCible.UNE_CARTE_ENNEMIE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )