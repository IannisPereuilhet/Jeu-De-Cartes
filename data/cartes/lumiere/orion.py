from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.electro_choc import electro_choc
from data.attaques.lumiere.magie_d_orion import magie_d_orion

def orion():
    return Carte(

        nom="ORION",

        numero=143,

        rarete=TypeRarete.RARE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            electro_choc(),
            magie_d_orion()
        ],

        passifs=None
    )