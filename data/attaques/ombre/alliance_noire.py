from utils import *
from src.attaque import Attaque
from src.effet import *

def alliance_noire():
    return Attaque(
        
        nom="ALLIANCE NOIRE",

        effets=[
            BONUS_ELEMENT(
                valeur=20,
                element=Element.OMBRE,
                cible=TypeCible.JOUEUR
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.FEU: 4,
                    Element.EAU: 4,
                    Element.NATURE: 4,
                    Element.TERRE: 4,
                    Element.OMBRE: 4,
                    Element.LUMIERE: 4
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.OMBRE
    )