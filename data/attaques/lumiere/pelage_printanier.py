from utils import *
from src.attaque import Attaque
from src.effet import *

def pelage_printanier():
    return Attaque(
    
        nom="PELAGE PRINTANIER",

        effets=[
            BONUS_ELEMENT(
                valeur=7,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
            )      
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    "PV": 100
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.LUMIERE
    )