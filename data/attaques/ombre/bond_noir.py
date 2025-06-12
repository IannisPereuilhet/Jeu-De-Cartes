from utils import *
from src.attaque import Attaque
from src.effet import *

def bond_noir():
    return Attaque(
        
        nom="BOND NOIR",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=[
            BONUS_ELEMENT(
                valeur=10,
                element=Element.OMBRE,
                cible=TypeCible.JOUEUR
            )
        ],

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.1,

        critique=2,

        recharge=1,

        element=Element.OMBRE
    )