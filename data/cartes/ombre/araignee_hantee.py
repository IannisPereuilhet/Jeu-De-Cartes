from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.clair_obscur import clair_obscur
from data.attaques.ombre.tissage import tissage

def araignee_hantee():
    return Carte(

        nom="ARAIGNEE HANTE",

        numero=129,

        rarete=TypeRarete.COMMUNE,

        pv=425,

        element=Element.OMBRE,

        attaques=[
            clair_obscur(),
            tissage()
        ],

        passifs=None
    )