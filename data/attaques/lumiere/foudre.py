from utils import *
from src.attaque import Attaque
from src.effet import *

def foudre():
    return Attaque(
    
        nom="FOUDRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.PV_BAS
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.15,

        critique=2,

        recharge=2,

        element=Element.LUMIERE
    )