from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.feu.morsure_brulante import morsure_brulante
from data.attaques.feu.sol_enflamme import sol_enflamme

def roi_des_flammes_ardentes():
    return Carte(

        nom="ROI DES FLAMMES ARDENTES",

        numero=37,

        rarete=TypeRarete.EPIQUE,

        pv=450,

        element=Element.FEU,

        attaques=[
            morsure_brulante(),
            sol_enflamme()
        ],

        passifs=None
    )