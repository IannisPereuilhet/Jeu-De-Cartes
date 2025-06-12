from utils import *
from src.attaque import Attaque
from src.effet import *

def magie_de_lyra():
    return Attaque(
    
        nom="MAGIE DE LYRA",

        effets=[
            BONUS_ELEMENT(
                valeur=2,
                element=Element.ALEATOIRE,
                cible=TypeCible.JOUEUR
            ),

             PROBA_CRITIQUE(
                 valeur=0.5,
                 cible=TypeCible.UNE_CARTE_ALLIEE,
                 element_cond=Element.LUMIERE
             )     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )