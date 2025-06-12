from utils import *
from src.attaque import Attaque
from src.effet import *

def vague_de_sable():
    return Attaque(
    
        nom="VAGUE DE SABLE",

        effets=[
            DEGATS_ELEMENT(
                valeur=15,
                element=Element.TERRE,
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
                valeur=-0.05,
                cible=TypeCible.UNE_CARTE_ENNEMIE
            ),      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.TERRE
    )