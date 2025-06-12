from utils import *
from src.attaque import Attaque
from src.effet import *

def fin_du_monde():
    return Attaque(
    
        nom="FIN DU MONDE",

        effets=[
            DEGATS_ELEMENT(
                valeur=70,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=70,
                element=Element.EAU,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=70,
                element=Element.NATURE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=70,
                element=Element.OMBRE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=70,
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

        recharge=8,

        element=Element.TERRE
    )