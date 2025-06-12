from utils import *
from src.attaque import Attaque
from src.effet import *

def appel_de_la_lumiere():
    return Attaque(
    
        nom="APPEL DE LA LUMIERE",

        effets=[
            PROBA_PRECISION(
                valeur=1.0,
                cible=TypeCible.TOUS_LES_ALLIES
            ) 
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=7,

        element=Element.LUMIERE
    )