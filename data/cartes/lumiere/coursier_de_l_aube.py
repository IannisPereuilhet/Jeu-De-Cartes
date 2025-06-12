from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.course_folle import course_folle

def coursier_de_l_aube():
    return Carte(

        nom="COURISER DE L'AUBE",

        numero=66,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            course_folle()
        ],

        passifs=None
    )