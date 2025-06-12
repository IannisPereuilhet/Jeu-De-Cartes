from utils import *
from src.attaque import Attaque
from src.effet import *

def flash():
    return Attaque(
    
        nom="FLASH",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=[
            ETOURDISSEMENT(
                duree=1
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.LUMIERE
    )