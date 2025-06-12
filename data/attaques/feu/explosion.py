from utils import *
from src.attaque import Attaque
from src.effet import *

def explosion():
    return Attaque(
    
        nom="EXPLOSION",

        effets=[
            DEGATS_ELEMENT(
                valeur=150,
                element=Element.FEU,
                cible=TypeCible.UNE_CARTE,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.FEU: 5,
                    Element.EAU: 5,
                    Element.NATURE: 5,
                    Element.TERRE: 5,
                    Element.OMBRE: 5,
                    Element.LUMIERE: 5
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=2,

        element=Element.FEU
    )