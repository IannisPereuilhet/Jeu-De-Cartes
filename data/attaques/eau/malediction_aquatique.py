from utils import *
from src.attaque import Attaque
from src.effet import *

def malediction_aquatique():
    return Attaque(
    
        nom="MALEDICTION AQUATIQUE",

        effets=[
            [
                DEGATS_ELEMENT(
                    valeur=40,
                    element=Element.EAU,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                ),

                DEGATS_ELEMENT(
                    valeur=40,
                    element=Element.NATURE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                ),
                
                ETOURDISSEMENT(
                    duree=1,
                    cible=TypeCible.UNE_CARTE
                )
            ],

            [
                DEGATS_ELEMENT(
                    valeur=40,
                    element=Element.EAU,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                ),

                DEGATS_ELEMENT(
                    valeur=40,
                    element=Element.NATURE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                ),

                DISPARITION(
                    cible=TypeCible.UNE_CARTE
                )
            ]    
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=6,

        element=Element.EAU
    )