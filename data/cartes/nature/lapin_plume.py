from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.son_percant import son_percant

def lapin_plume():
    return Carte(

        nom="LAPIN PLUME",

        numero=158,

        rarete=TypeRarete.COMMUNE,

        pv=550,

        element=Element.NATURE,

        attaques=[
            son_percant()
        ],

        passifs=[
            SAC_DE_FRAPPE()
        ]
    )