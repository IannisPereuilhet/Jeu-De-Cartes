from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.genie_incompris import genie_incompris
from data.attaques.ombre.clair_obscur import clair_obscur

def le_gamin_des_etoiles():
    return Carte(

        nom="LE GAMIN DES ETOILES",

        numero=36,

        rarete=TypeRarete.RARE,

        pv=500,

        element=Element.LUMIERE,

        attaques=[
            genie_incompris(),
            clair_obscur()
        ],

        passifs=None
    )