from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.lumiere_artificielle import lumiere_artificielle
from data.attaques.lumiere.appel_de_la_lumiere import appel_de_la_lumiere
from data.attaques.lumiere.lumiere_precise import lumiere_precise

def l_artiste_des_cieux():
    return Carte(

        nom="L'ARTISTE DES CIEUX",

        numero=48,

        rarete=TypeRarete.LEGENDAIRE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            lumiere_artificielle(),
            appel_de_la_lumiere(),
            lumiere_precise()
        ],

        passifs=None
    )