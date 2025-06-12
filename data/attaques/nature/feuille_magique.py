from utils import *
from src.attaque import Attaque
from src.effet import *

def feuille_magique():
    return Attaque(
    
        nom="FEUILLE MAGIQUE",

        effets=[
            SOIN_ELEMENT(
                valeur=10,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PV_MAX(
                valeur=10,
                cible=TypeCible.UNE_CARTE
            )
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.25,

        critique=3,

        recharge=1,

        element=Element.NATURE
    )