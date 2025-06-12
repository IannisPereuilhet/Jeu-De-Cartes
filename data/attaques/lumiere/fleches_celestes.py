from utils import *
from src.attaque import Attaque
from src.effet import *

def fleches_celestes():
    return Attaque(
        
        nom="FLECHES CELESTES",

        effets=[
            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),  

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE_ENNEMIE,
                calcul=TypeCalcul.CLASSIQUE
            ),

            DEGATS_ELEMENT(
                valeur=3,
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

        proba_critique=0.25,

        critique=2,

        recharge=2,

        element=Element.LUMIERE
    )