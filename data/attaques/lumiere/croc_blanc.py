from utils import *
from src.attaque import Attaque
from src.effet import *

def croc_blanc():
    return Attaque(
    
        nom="CROC-BLANC",

        effets=[
            DEGATS_ELEMENT(
                valeur=25,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_CRITIQUE(
                valeur=0.05,
                cible=TypeCible.SOI_MEME
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.LUMIERE
    )