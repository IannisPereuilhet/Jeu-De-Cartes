from utils import *
from src.attaque import Attaque
from src.effet import *

def course_folle():
    return Attaque(
    
        nom="COURSE FOLLE",

        effets=[
            DEGATS_ELEMENT(
                valeur=60,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=-0.2,
                cible=TypeCible.SOI_MEME
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.LUMIERE
    )