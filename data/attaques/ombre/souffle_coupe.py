from utils import *
from src.attaque import Attaque
from src.effet import *

def souffle_coupe():
    return Attaque(
    
        nom="SOUFFLE COUPE",

        effets=[
            [
                PURGE(
                    cible=TypeCible.UNE_CARTE
                )
            ],
            
            [
                DEGATS_ELEMENT(
                    valeur=70,
                    element=Element.OMBRE,
                    cible=TypeCible.TOUTES_LES_CARTES,
                    calcul=TypeCalcul.CLASSIQUE
                )
            ]      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=7,

        element=Element.OMBRE
    )