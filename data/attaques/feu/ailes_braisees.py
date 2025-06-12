from utils import *
from src.attaque import Attaque
from src.effet import *

def ailes_braisees():
    return Attaque(
    
        nom="AILES BRAISEES",

        effets=[
            DEGATS_ELEMENT(
                valeur=35,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=35,
                element=Element.NATURE,
                cible=TypeCible.SOI_MEME,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=0.08,
                cible=TypeCible.TOUS_LES_ALLIES
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.FEU
    )