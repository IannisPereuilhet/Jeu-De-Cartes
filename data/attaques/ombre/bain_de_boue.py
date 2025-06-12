from utils import *
from src.attaque import Attaque
from src.effet import *

def bain_de_boue():
    return Attaque(
        
        nom="BAIN DE BOUE",

        effets=[
            DEGATS_ELEMENT(
                valeur=30,
                element=Element.OMBRE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            POISON()
        ],

        proba_precision=1.0,

        proba_critique=0.1,

        critique=2,

        recharge=5,

        element=Element.OMBRE
    )