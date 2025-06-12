from utils import *
from src.attaque import Attaque
from src.effet import *

def chaleur_divine():
    return Attaque(
    
        nom="CHALEUR DIVINE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=3,

        recharge=4,

        element=Element.FEU
    )