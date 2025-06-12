from utils import *
from src.attaque import Attaque
from src.effet import *

def eclat():
    return Attaque(
    
        nom="ECLAT",

        effets=[
            DEGATS_ELEMENT(
                valeur=25,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=[
            ALEATOIRE()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )