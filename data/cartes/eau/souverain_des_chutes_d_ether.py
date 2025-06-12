from utils import *
from src.carte import Carte
from src.effet import *
from data.attaques.eau.laser_glacial import laser_glacial
from data.attaques.eau.chute_critique import chute_critique 
from data.attaques.ombre.chute_precise import chute_precise

def souverain_des_chutes_d_ether():
    return Carte(

        nom="SOUVERAIN DES CHUTES D'ETHER",

        numero=136,

        rarete=TypeRarete.RARE,        

        pv=400,

        element=Element.EAU,

        attaques=[
            laser_glacial(),
            chute_critique(),
            chute_precise()
        ],

        passifs=None,
    )