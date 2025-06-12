from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.lumiere.fleches_celestes import fleches_celestes
from data.attaques.lumiere.jugement_divin import jugement_divin
from data.attaques.lumiere.lumiere_critique import lumiere_critique

def melodie_des_divinites():
    return Carte(

        nom="MELODIE DES DIVINITES",

        numero=96,

        rarete=TypeRarete.LEGENDAIRE,

        pv=450,

        element=Element.LUMIERE,

        attaques=[
            fleches_celestes(),
            jugement_divin(),
            lumiere_critique()
        ],

        passifs=None
    )