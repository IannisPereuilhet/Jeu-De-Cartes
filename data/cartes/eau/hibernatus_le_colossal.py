from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.frappe_glaciale import frappe_glaciale
from data.attaques.terre.racine_pointue import racine_pointue

def hibernatus_le_colossal():
    return Carte(

        nom="HIBERNATUS LE COLOSSAL",

        numero=171,

        rarete=TypeRarete.COMMUNE,

        pv=500,

        element=Element.EAU,

        attaques=[
            frappe_glaciale(),
            racine_pointue()
        ],

        passifs=[
            VENGEUR()
        ]
    )