from utils import *
from src.attaque import Attaque
from src.effet import *

def eclat_paisible():
    return Attaque(
    
        nom="ECLAT PAISIBLE",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            VOL_ELEMENT(
                valeur=1,
                element=Element.LUMIERE,
                cible=TypeCible.ADVERSAIRE
            )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )