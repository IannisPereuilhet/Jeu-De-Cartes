from utils import *
from src.attaque import Attaque
from src.effet import *

def pleur():
    return Attaque(
    
        nom="PLEUR",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            VOL_ELEMENT(
                valeur=1,
                element=Element.OMBRE,
                cible=TypeCible.ADVERSAIRE
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.OMBRE
    )