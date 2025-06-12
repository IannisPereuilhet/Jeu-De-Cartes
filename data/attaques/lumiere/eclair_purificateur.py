from utils import *
from src.attaque import Attaque
from src.effet import *

def eclair_purificateur():
    return Attaque(
        
        nom="ECLAIR PURIFICATEUR",

        effets=[
            DEGATS_ELEMENT(
                valeur=40,
                element=Element.LUMIERE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            ZONE()
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=4,

        element=Element.LUMIERE
    )