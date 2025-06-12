from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.ombre.idee_sombre import idee_sombre
from data.attaques.ombre.souffle_coupe import souffle_coupe

def l_epouvante_hesitante():
    return Carte(

        nom="L'EPOUVANTE HESITANTE",

        numero=111,

        rarete=TypeRarete.COMMUNE,

        pv=400,

        element=Element.OMBRE,

        attaques=[
            idee_sombre(),
            souffle_coupe()
        ],

        passifs=None
    )