from utils import *
from src.attaque import Attaque
from src.effet import *

def feu_sombre():
    return Attaque(
    
        nom="FEU SOMBRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.FEU
    )