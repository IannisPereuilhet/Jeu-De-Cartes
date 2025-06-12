from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.concerto import concerto

def sarah_melodie_marine():
    return Carte(

        nom="SARAH, MELODIE MARINE",

        numero=184,

        rarete=TypeRarete.RARE,        

        pv=375,

        element=Element.EAU,

        attaques=[
            concerto()
        ],

        passifs=[
            SAC_DE_FRAPPE(),
            TENACITE()
        ]
    )