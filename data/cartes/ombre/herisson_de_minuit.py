from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.pic_toxique import pic_toxique

def herisson_de_minuit():
    return Carte(

        nom="HERISSON DE MINUIT",

        numero=149,

        rarete=TypeRarete.EPIQUE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            pic_toxique()
        ],

        passifs=[
            POISON(),

            RENVOI()
        ]
    )