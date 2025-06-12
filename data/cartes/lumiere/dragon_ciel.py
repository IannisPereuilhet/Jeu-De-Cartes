from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.souffle_eblouissant import souffle_eblouissant
from data.attaques.nature.souffle_tornade import souffle_tornade

def dragon_ciel():
    return Carte(

        nom="DRAGON CIEL",

        numero=180,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.LUMIERE,

        attaques=[
            souffle_eblouissant(),
            souffle_tornade()
        ],

        passifs=[
            VENGEUR()
        ]
    )