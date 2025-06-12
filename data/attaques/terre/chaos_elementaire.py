from utils import *
from src.attaque import Attaque
from src.effet import *

def chaos_elementaire():
    return Attaque(
    
        nom="CHAOS ELEMENTAIRE",

        effets=[
            DEGATS_ELEMENT(
                valeur=15,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=15,
                element=Element.LUMIERE,
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

        recharge=3,

        element=Element.TERRE
    )