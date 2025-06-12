from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.fort import fort

def le_transporteur_sauvage():
    return Carte(

        nom="LE TRANSPORTEUR SAUVAGE",

        numero=58,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.TERRE,

        attaques=[
            fort()
        ],

        passifs=[
            SAC_DE_FRAPPE()
        ]
    )