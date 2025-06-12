from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.pluie_elementaire import pluie_elementaire
from data.attaques.nature.drain_vital import drain_vital

def saule_ardent():
    return Carte(

        nom="SAULE ARDENT",

        numero=145,

        rarete=TypeRarete.EPIQUE,

        pv=500,

        element=Element.FEU,

        attaques=[
            pluie_elementaire(),
            drain_vital()
        ],

        passifs=None
    )