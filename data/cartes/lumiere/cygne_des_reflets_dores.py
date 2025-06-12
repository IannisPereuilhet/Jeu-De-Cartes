from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.vent_argente import vent_argente
from data.attaques.lumiere.lumiere_critique import lumiere_critique

def cygne_des_reflets_dores():
    return Carte(

        nom="CYGNE DES REFLETS DORES",

        numero=113,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.LUMIERE,

        attaques=[
            vent_argente(),
            lumiere_critique()
        ],

        passifs=None
    )