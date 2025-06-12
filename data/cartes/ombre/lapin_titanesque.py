from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.boule_de_haine import boule_de_haine

def lapin_titanesque():
    return Carte(

        nom="LAPIN TITANESQUE",

        numero=128,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.OMBRE,

        attaques=[
            boule_de_haine()
        ],

        passifs=None
    )