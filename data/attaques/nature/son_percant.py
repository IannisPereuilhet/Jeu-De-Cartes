from utils import *
from src.attaque import Attaque
from src.effet import *

def son_percant():
    return Attaque(
    
        nom="SON PERCANT",

        effets=[
            DEGATS_ELEMENT(
                valeur=3,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ) 
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=5
            ),

            COUT(
                cout={
                    "PV": 10
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.NATURE
    )