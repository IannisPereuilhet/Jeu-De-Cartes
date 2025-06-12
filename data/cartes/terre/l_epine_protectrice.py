from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.fracas_tellurique import fracas_tellurique
from data.attaques.terre.rempart_elementaire import rempart_elementaire

def l_epine_protectrice():
    return Carte(

        nom="L'EPINE PROTECTRICE",

        numero=40,

        rarete=TypeRarete.EPIQUE,

        pv=425,

        element=Element.TERRE,

        attaques=[
            fracas_tellurique(),
            rempart_elementaire()
        ],

        passifs=[
            RENVOI()
        ]
    )