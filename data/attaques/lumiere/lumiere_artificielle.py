from utils import *
from src.attaque import Attaque
from src.effet import *

def lumiere_artificielle():
    return Attaque(
    
        nom="LUMIERE ARTIFICIELLE",

        effets=[
            DEGATS_ELEMENT(
                valeur=100,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=0.01,

        proba_critique=0.05,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )