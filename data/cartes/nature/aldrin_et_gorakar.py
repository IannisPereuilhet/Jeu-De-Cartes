from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.nature.valse_des_nuages import valse_des_nuages
from data.attaques.nature.souffle_critique import souffle_critique 
from data.attaques.terre.pietinement import pietinement 

def aldrin_et_gorakar():
    return Carte(

        nom="ALDRIN ET GORAKAR",

        numero=45,

        rarete=TypeRarete.LEGENDAIRE,

        pv=400,

        element=Element.NATURE,

        attaques=[
            valse_des_nuages(),
            souffle_critique(),
            pietinement()
        ],

        passifs=None
    )