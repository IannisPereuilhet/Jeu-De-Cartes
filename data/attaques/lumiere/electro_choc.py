from utils import *
from src.attaque import Attaque
from src.effet import *

def electro_choc():
    return Attaque(
        
        nom="ELECTRO-CHOC",

        effets=[
            DEGATS_ELEMENT(
                valeur=20,
                element=Element.LUMIERE,
                cible=TypeCible.TOUS_LES_ENNEMIS,
                calcul=TypeCalcul.CLASSIQUE
            )    
        ],

        effets_critiques=None,

        effets_passifs=[
            COUT(
                cout={
                    Element.LUMIERE: 2
                }
            )
        ],

        proba_precision=0.5,

        proba_critique=0.5,

        critique=2,

        recharge=1,

        element=Element.LUMIERE
    )