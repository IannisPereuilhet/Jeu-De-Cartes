from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.visee_globale import visee_globale
from data.attaques.ombre.visee_offensive import visee_offensive
from data.attaques.terre.multiboost import multiboost

def chouette_prismatique():
    return Carte(

        nom="CHOUETTE PRISMATIQUE",

        numero=88,

        rarete=TypeRarete.EPIQUE,

        pv=450,

        element=Element.OMBRE,

        attaques=[
            visee_globale(),
            visee_offensive(),
            multiboost()
        ],

        passifs=None
    )