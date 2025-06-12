from utils import *
from src.attaque import Attaque
from src.effet import *

def arc_en_ciel():
    return Attaque(
    
        nom="ARC-EN-CIEL",

        effets=[
            [
                DEGATS_ELEMENT(
                    valeur=20,
                    element=Element.ALEATOIRE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                )
            ],

            [
                SOIN_ELEMENT(
                    valeur=20,
                    element=Element.ALEATOIRE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                ),
            ]
                 
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.50,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )