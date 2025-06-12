from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.tenebres import tenebres
from data.attaques.lumiere.lumieres import lumieres

def l_oiseau_de_la_dualite():
    return Carte(

        nom="L'OISEAU DE LA DUALITE",

        numero=150,

        rarete=TypeRarete.EPIQUE,

        pv=400,

        element=Element.LUMIERE,

        attaques=[
            tenebres(),
            lumieres()
        ],

        passifs=None
    )