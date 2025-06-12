from utils import *
from src.attaque import Attaque
from src.effet import *

def visee_globale():
    return Attaque(
    
        nom="VISEE GLOBALE",

        effets=[
            ETERNITE(
                valeur=1,
                cible=TypeCible.TOUS_LES_ENNEMIS
            )    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=8,

        element=Element.OMBRE
    )