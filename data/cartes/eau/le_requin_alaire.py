from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.aquapique import aquapique
from data.attaques.terre.rempart_elementaire import rempart_elementaire

def le_requin_alaire():
    return Carte(

        nom="LE REQUIN ALAIRE",

        numero=70,

        rarete=TypeRarete.RARE,

        pv=465,

        element=Element.EAU,

        attaques=[
            aquapique(),
            rempart_elementaire()
        ],

        passifs=None
    )