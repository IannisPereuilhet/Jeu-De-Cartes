from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.flanerie import flanerie

def errance_du_manoir():
    return Carte(

        nom="ERRANCE DU MANOIR",

        numero=110,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            flanerie()
        ],

        passifs=[
            POISON()
        ]
    )