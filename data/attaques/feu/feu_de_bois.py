from utils import *
from src.attaque import Attaque
from src.effet import *

def feu_de_bois():
    return Attaque(
    
        nom="FEU DE BOIS",

        effets=[
            DEGATS_ELEMENT(
                valeur=5,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            ALEATOIRE()
        ],

        proba_precision=1.0,

        proba_critique=0.50,

        critique=2,

        recharge=2,

        element=Element.FEU
    )