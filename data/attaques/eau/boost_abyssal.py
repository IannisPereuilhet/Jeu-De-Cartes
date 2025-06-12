from utils import *
from src.attaque import Attaque
from src.effet import *

def boost_abyssal():
    return Attaque(
    
        nom="BOOST ABYSSAL",

        effets=[
            VALEUR_DE_BASE(
                valeur=1,
                cible=TypeCible.TOUS_LES_ALLIES
            )  
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.EAU
    )