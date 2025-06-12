from utils import *
from src.attaque import Attaque
from src.effet import *

def marteau_lumineux():
    return Attaque(
    
        nom="MARTEAU LUMINEUX",

        effets=[
            DEGATS_ELEMENT(
                valeur=15,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_PRECISION(
                valeur=0.1,
                cible=TypeCible.TOUS_LES_ALLIES
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.LUMIERE
    )