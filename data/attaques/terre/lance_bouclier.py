from utils import *
from src.attaque import Attaque
from src.effet import *

def lance_bouclier():
    return Attaque(
    
        nom="LANCE-BOUCLIER",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=10,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            BONUS_ELEMENT(
                valeur=4,
                element=Element.LUMIERE,
                cible=TypeCible.JOUEUR
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.TERRE
    )