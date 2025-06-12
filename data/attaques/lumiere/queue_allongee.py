from utils import *
from src.attaque import Attaque
from src.effet import *

def queue_allongee():
    return Attaque(
    
        nom="QUEUE ALLONGEE",

        effets=[
            DEGATS_ELEMENT(
                valeur=40,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=40,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            RECHARGE_MOD(
                valeur=1,
                cible=TypeCible.SOI_MEME
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