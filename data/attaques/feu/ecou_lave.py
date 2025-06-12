from utils import *
from src.attaque import Attaque
from src.effet import *

def ecou_lave():
    return Attaque(
    
        nom="ECOU-LAVE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=[
            POISON()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=5,

        recharge=1,

        element=Element.FEU
    )