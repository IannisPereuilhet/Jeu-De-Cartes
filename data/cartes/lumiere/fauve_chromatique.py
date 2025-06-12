from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.terre.chaos_elementaire import chaos_elementaire
from data.attaques.lumiere.multilucky import multilucky

def fauve_chromatique():
    return Carte(

        nom="FAUVE CHROMATIQUE",

        numero=179,

        rarete=TypeRarete.COMMUNE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            chaos_elementaire(),
            multilucky()
        ],

        passifs=None
    )