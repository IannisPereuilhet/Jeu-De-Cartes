from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.soin_tribu import soin_tribu
from data.attaques.feu.incaflamme import incaflamme

def chaman_brule_guerre():
    return Carte(

        nom="CHAMAN BRULE-GUERRE",

        numero=170,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.FEU,

        attaques=[  
            soin_tribu(),
            incaflamme()
        ],

        passifs=[
            SOIN_PRIMITIF()
        ]
    )