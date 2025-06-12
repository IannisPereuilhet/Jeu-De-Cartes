from utils import *
from src.attaque import Attaque
from src.effet import *

def grain_de_sable():
    return Attaque(
    
        nom="GRAIN DE SABLE",

        effets=[
            DEGATS_ELEMENT(
                valeur=10,
                element=Element.TERRE,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )  
        ],

        effets_critiques=[
            ETOURDISSEMENT(
                duree=1,
                cible=TypeCible.UNE_CARTE)
        ],

        effets_passifs=[
            RECHARGE_PROBA(
                valeur=0.5
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=1,

        element=Element.TERRE
    )