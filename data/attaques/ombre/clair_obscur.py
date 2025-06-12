from utils import *
from src.attaque import Attaque
from src.effet import *

def clair_obscur():
    return Attaque(
    
        nom="CLAIR-OBSCUR",

        effets=[
            DEGATS_ELEMENT(
                valeur=40,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            SOIN_ELEMENT(
                valeur=40,
                element=Element.LUMIERE,
                cible=TypeCible.SOI_MEME,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.OMBRE
    )