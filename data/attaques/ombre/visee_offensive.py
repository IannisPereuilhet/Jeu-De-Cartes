from utils import *
from src.attaque import Attaque
from src.effet import *

def visee_offensive():
    return Attaque(
    
        nom="VISEE OFFENSIVE",

        effets=[
            DEGATS_ELEMENT(
                valeur=15,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=[
            ETERNITE(
                valeur=1,
                cible=TypeCible.UNE_CARTE),
        ],

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.5,

        critique=2,

        recharge=2,

        element=Element.OMBRE
    )