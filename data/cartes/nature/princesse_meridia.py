from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.vent_critique import vent_critique
from data.attaques.nature.volupte import volupte

def princesse_meridia():
    return Carte(

        nom="PRINCESSE MERIDIA",

        numero=29,

        rarete=TypeRarete.RARE,

        pv=425,

        element=Element.NATURE,

        attaques=[
            vent_critique(),
            volupte()
        ],

        passifs=None
    )