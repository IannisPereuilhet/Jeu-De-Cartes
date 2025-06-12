from utils import *
from src.attaque import Attaque
from src.effet import *

def aqua_sombre():
    return Attaque(
    
        nom="AQUA-SOMBRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=20,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ), 

            ETOURDISSEMENT(
                duree=1,
                cible=TypeCible.UNE_CARTE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.EAU
    )