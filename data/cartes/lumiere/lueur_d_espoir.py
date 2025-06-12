from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.soin_critique import soin_critique
from data.attaques.lumiere.ecran import ecran

def lueur_d_espoir():
    return Carte(

        nom="LUEUR D'ESPOIR",

        numero=22,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.LUMIERE,

        attaques=[
            soin_critique(),
            ecran()
        ],

        passifs=None
    )