from utils import *
from src.attaque import Attaque
from src.effet import *

def lucky_fire():
    return Attaque(
    
        nom="LUCKY-FIRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=7,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=7,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=7,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            RECHARGE_PROBA(
                valeur=0.5
            ),

            VAMPIRISME()
        ],

        proba_precision=0.5,

        proba_critique=0.5,

        critique=2,

        recharge=1,

        element=Element.FEU
    )