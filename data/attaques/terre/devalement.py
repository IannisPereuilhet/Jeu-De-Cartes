from utils import *
from src.attaque import Attaque
from src.effet import *

def devalement():
    return Attaque(
    
        nom="DEVALEMENT",

        effets=[
            DEGATS_ELEMENT(
                valeur=25,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=None,

        effets_passifs=[
            ALEATOIRE()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )