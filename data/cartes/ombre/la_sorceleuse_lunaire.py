from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.soin_d_ombre import soin_d_ombre
from data.attaques.ombre.faible_lune import faible_lune
from data.attaques.ombre.visee import visee

def la_sorceleuse_lunaire():
    return Carte(

        nom="LA SORCELEUSE LUNAIRE",

        numero=61,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            soin_d_ombre(),
            faible_lune(),
            visee()
        ],

        passifs=None
    )