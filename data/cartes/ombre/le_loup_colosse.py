from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.percee_nocturne import percee_nocturne
from data.attaques.ombre.pleur import pleur

def le_loup_colosse():
    return Carte(

        nom="LE LOUP COLOSSE",

        numero=87,

        rarete=TypeRarete.EPIQUE,

        pv=350,

        element=Element.OMBRE,

        attaques=[
            percee_nocturne(),
            pleur()
        ],

        passifs=None
    )