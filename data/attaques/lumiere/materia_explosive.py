from utils import *
from src.attaque import Attaque
from src.effet import *

def materia_explosive():
    return Attaque(
    
        nom="MATERIA EXPLOSIVE",

        effets=[
            DEGATS_ELEMENT(
                valeur=[1, 100],
                element=Element.ALEATOIRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=3,

        recharge=3,

        element=Element.LUMIERE
    )