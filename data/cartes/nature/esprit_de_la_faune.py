from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.appel_de_la_foret import appel_de_la_foret
from data.attaques.lumiere.soin_soleil import soin_soleil

def esprit_de_la_faune():
    return Carte(

        nom="ESPRIT DE LA FAUNE",

        numero=122,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.NATURE,

        attaques=[
            appel_de_la_foret(),
            soin_soleil()
        ],

        passifs=None
    )