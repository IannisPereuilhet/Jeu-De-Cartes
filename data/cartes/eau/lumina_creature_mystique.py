from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.riposte import riposte
from data.attaques.eau.bulles import bulles

def lumina_creature_mystique():
    return Carte(

        nom="LUMINA, CREATURE MYSTIQUE",

        numero=38,
        
        rarete=TypeRarete.EPIQUE,

        pv=425,

        element=Element.EAU,

        attaques=[
            riposte(),
            bulles()
        ],

        passifs=[
            EROSION()
        ]
    )