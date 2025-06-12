from utils import *
from src.attaque import Attaque
from src.effet import *

def controle_de_terre():
    return Attaque(
    
        nom="CONTROLE DE TERRE",

        effets=[
            BONUS_ELEMENT(
                valeur=6,
                element=Element.TERRE,
                cible=TypeCible.TOUS_LES_JOUEURS
            )      
        ],

        effets_critiques=None,

        effets_passifs=None,

        proba_precision=1.0,

        proba_critique=0.01,

        critique=2,

        recharge=3,

        element=Element.TERRE
    )