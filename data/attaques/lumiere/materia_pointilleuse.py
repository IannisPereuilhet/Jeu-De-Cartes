from utils import *
from src.attaque import Attaque
from src.effet import *

def materia_pointilleuse():
    return Attaque(
    
        nom="MATERIA POINTILLEUSE",

        effets=[
            [
                PROBA_CRITIQUE(
                    valeur=0.15,
                    cible=TypeCible.UNE_CARTE_ALLIEE
                )
            ],

            [
                PROBA_PRECISION(
                    valeur=0.15,
                    cible=TypeCible.UNE_CARTE_ALLIEE
                )
            ]      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.LUMIERE
    )