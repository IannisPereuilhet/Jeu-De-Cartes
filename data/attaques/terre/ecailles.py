from utils import *
from src.attaque import Attaque
from src.effet import *

def ecailles():
    return Attaque(
    
        nom="ECAILLES",

        effets=[
            DEGATS_ELEMENT(
                valeur=5,
                element=Element.ALEATOIRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=5,
                element=Element.ALEATOIRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=5,
                element=Element.ALEATOIRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            VALEUR_DE_BASE(
                valeur=1,
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )