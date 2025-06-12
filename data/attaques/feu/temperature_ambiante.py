from utils import *
from src.attaque import Attaque
from src.effet import *

def temperature_ambiante():
    return Attaque(
    
        nom="TEMPERATURE AMBIANTE",

        effets=[
            BONUS_ELEMENT(
                valeur=20,
                element=Element.FEU,
                cible=TypeCible.JOUEUR
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=7,

        element=Element.FEU
    )