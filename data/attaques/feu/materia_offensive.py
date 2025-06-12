from utils import *
from src.attaque import Attaque
from src.effet import *

def materia_offensive():
    return Attaque(
    
        nom="MATERIA OFFENSIVE",

        effets=[
            [
                DEGATS_ELEMENT(
                    valeur=40,
                    element=Element.FEU,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                )
            ],

            [
                DEGATS_ELEMENT(
                    valeur=40,
                    element=Element.LUMIERE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                )
            ],

            [
                DEGATS_ELEMENT(
                    valeur=40,
                    element=Element.NATURE,
                    cible=TypeCible.UNE_CARTE,
                    calcul=TypeCalcul.CLASSIQUE
                )
            ]     
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.FEU
    )