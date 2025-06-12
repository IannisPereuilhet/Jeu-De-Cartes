from utils import *

from src.carte import *
from src.attaque import *
from src.effet import *

from src.joueur import *



calcul = TypeCalcul.MULTIPLICATEUR_ELEMENT
calcul = TypeCalcul.CLASSIQUE

effet_1 = DEGATS_ELEMENT(valeur=10, element=Element.ALEATOIRE, cible=TypeCible.UNE_CARTE_ENNEMIE, calcul=calcul)
effet_2 = BONUS_ELEMENT(valeur=5, element=Element.ALEATOIRE, cible=TypeCible.JOUEUR)
effet_3 = SOIN_ELEMENT(valeur=10, element=Element.ALEATOIRE, cible=TypeCible.ALEATOIRE_ALLIE)
effet_4 = PROBA_PRECISION(valeur=[-0.1, -0.3], cible=TypeCible.ALEATOIRE_ENNEMI) 
effet_5 = PROBA_CRITIQUE(valeur=0.8, cible=effet_1.cible) 
effet_6 = DEGATS_CRITIQUE(valeur=5, cible=effet_1.cible)  
effet_7 = DEGATS_POURCENTAGE(valeur=0.33, cible=TypeCible.UNE_CARTE)
effet_8 = TEMPORALITE(cible=TypeCible.UNE_CARTE)
effet_9 = ETERNITE(cible=TypeCible.UNE_CARTE)
effet_10 = SOIN_POURCENTAGE(valeur=0.8, cible=TypeCible.UNE_CARTE)
effet_11 = VOL_ELEMENT(valeur=5, element=Element.ALEATOIRE)
effet_13 = RECHARGE_MAX(cible=TypeCible.UNE_CARTE)
effet_14 = RECHARGE_RENIT(cible=TypeCible.UNE_CARTE)
effet_15 = PV_MAX(valeur=-50, cible=TypeCible.UNE_CARTE)
effet_16 = DISPARITION(cible=TypeCible.UNE_CARTE)
effet_17 = PROVOCATION(cible=TypeCible.UNE_CARTE)
effet_18 = ETOURDISSEMENT(cible=TypeCible.UNE_CARTE)
effet_29 = VALEUR_DE_BASE(valeur=[1, 5], cible=TypeCible.ALEATOIRE_ALLIE)
effet_20 = SACRIFICE(cible=TypeCible.UNE_CARTE)
effet_21 = PURGE(cible=TypeCible.UNE_CARTE)
effet_22 = RESURRECTION(cible=TypeCible.UNE_CARTE)
effet_23 = RECHARGE_PROBA(valeur=0.5, cible=TypeCible.ATTAQUE)
effet_24 = RECHARGE_MOD(valeur=1, cible=TypeCible.ATTAQUE)
effet_25 = REPARTITION_PV(cible=TypeCible.JOUEUR)
effet_26 = PV_POURCENTAGE(valeur=0.5, cible=TypeCible.ALEATOIRE_ENNEMI)
effet_27 = VOL_PV(valeur=10, cible=TypeCible.ALEATOIRE_ENNEMI)
effet_28 = VOL_PV_MAX(valeur=10, cible=TypeCible.ALEATOIRE_ENNEMI)

passif_1 = RESET()
passif_2 = VENGEUR()
passif_3 = REVANCHE()
passif_4 = CIMETIERE()
passif_5 = TENACITE()
passif_6 = SAC_DE_FRAPPE()
passif_7 = RENVOI()
passif_8 = VAMPIRISME()
passif_9 = CONTRECOUP()
passif_10 = EROSION()
passif_11 = TERRAIN()
passif_12 = SOIN_PRIMITIF()
passif_13 = MIMETISME()
passif_14 = MYSTERE()
passif_15 = FUMEE()
passif_16 = ZONE()
passif_17 = CROISSANCE()
passif_18 = MULTIPLICATEUR()
passif_19 = IMMUNITE()
passif_20 = POISON()


cout = {Element.EAU: "TOUS", Element.FEU: 5, "PV": 10}
# cout = {}

usage_limite = 2
# usage_limite = 0


passifs_1 = [MYTHIQUE()]
passifs_2 = []


effets_critiques = []
effets_critiques = []

effets_passifs = []
# effets_passifs = []



attaque_1 = Attaque(effets=[effet_1], proba_precision=1.0, proba_critique=0.1, critique=2, recharge=1, effets_critiques=effets_critiques, effets_passifs=effets_passifs)
attaque_2 = Attaque(effets=[copy.deepcopy(effet_1)], proba_precision=1.0, proba_critique=0.01, critique=2, recharge=1)
attaque_3 = Attaque(effets=[effet_3], proba_precision=1.0, proba_critique=0.01, critique=2, recharge=1)
attaque_4 = Attaque(effets=[copy.deepcopy(effet_3)], proba_precision=1.0, proba_critique=0.01, critique=2, recharge=1)

carte_1 = Carte(numero=1, pv=100, element=Element.LUMIERE, attaques=[attaque_1, attaque_2], passifs=passifs_1)
carte_2 = Carte(numero=2, pv=100, element=Element.EAU, attaques=[attaque_3, attaque_4], passifs=passifs_2)

carte_3 = copy.deepcopy(carte_1)
carte_3.nom = "Carte 3"
carte_4 = copy.deepcopy(carte_2)
carte_4.nom = "Carte 4"

carte_5 = copy.deepcopy(carte_1)
carte_5.nom = "Carte 5"

carte_6 = copy.deepcopy(carte_2)
carte_6.nom = "Carte 6"

carte_7 = copy.deepcopy(carte_1)
carte_7.nom = "Carte 7"

carte_8 = copy.deepcopy(carte_2)
carte_8.nom = "Carte 8"

# carte_1.pv = 50
carte_4.pv = 20

J1 = Joueur(nom="Joueur 1", cartes=[carte_1, carte_2]) #, carte_5, carte_6])
J2 = Joueur(nom="Joueur 2", cartes=[carte_3, carte_4]) #, carte_7, carte_8])



# valeur degat quand tue = pv restant ? (pour savoir %de soin ou de degats passifs) (modifier subrdegta et pvmax au besoin)
# ajouter effet.symbole pour tous les effets (à utiliser pour Mystere)
# check IMMUNITEX dans le cas où passif
# check VALEUR_DE_BASE

# Effets:
# - ✅ aléaoire (attaque)
# - ✅ cimetière (passif) 
# - ✅ contrecoup (passif)
# - ✅ cout (attaque)
# - ✅ disparition (passif + effet)
# - ✅ fumee (passif)
# - ✅ immunite (passif)
# - ✅ mimétisme (passif)
# - ✅ multiplicateur (passif)
# - ✅ mystère (passif)
# - ✅ poison (passif)
# - ✅ provocation (passif + effet)
# - ✅ purge (effet + passif)
# - ✅ renvoi (passif)
# - ✅ reset (passif)
# - ✅ revanche (passif)
# - ✅ sac de frappe (passif)
# - ✅ soin primitif (passif)
# - ✅ temporalite (passif + effet)
# - ✅ terrain (passif)
# - ✅ tenacite (passif)
# - ✅ usage limite (attaque)
# - ✅ vampirisme (passif)
# - ✅ vengeur (passif)
# - ✅ erosion (passif)
# - ✅ eternite (passif + effet)
# - ✅ etourdissement (passif + effet)
# - ✅ zone (passif)

