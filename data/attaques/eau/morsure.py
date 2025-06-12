from utils import *
from src.attaque import Attaque
from src.effet import *

def morsure():
    return Attaque(
    
        nom="MORSURE",

        effets=[
            DEGATS_ELEMENT(
                valeur=6,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            PROBA_CRITIQUE(
                valeur=0.03,
                cible=TypeCible.TOUS_LES_ALLIES
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.5,

        critique=6,

        recharge=1,

        element=Element.EAU
    )