from utils import *
from src.attaque import Attaque
from src.effet import *

def boule_de_haine():
    return Attaque(
    
        nom="BOULE DE HAINE",

        effets=[
            DEGATS_ELEMENT(
                valeur=5,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )     
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=5
            ),

            VAMPIRISME()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.OMBRE
    )