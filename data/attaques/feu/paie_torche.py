from utils import *
from src.attaque import Attaque
from src.effet import *

def paie_torche():
    return Attaque(
        
        nom="PAIE-TORCHE",

        effets=[
            DISPARITION(
                cible=TypeCible.UNE_CARTE
            )   
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.FEU: 10
                }
            )
        ],

        proba_precision=1.0,

        proba_critique=0.05,

        critique=2,

        recharge=4,

        element=Element.FEU
    )