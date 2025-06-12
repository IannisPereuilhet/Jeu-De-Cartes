from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.dodo import dodo
from data.attaques.nature.eolienne import eolienne

def koala_fleuri():
    return Carte(

        nom="KOALA FLEURI",

        numero=104,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            dodo(),
            eolienne()
        ],

        passifs=[
            TERRAIN()
        ]
    )